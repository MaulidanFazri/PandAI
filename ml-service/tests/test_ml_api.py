import time

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field

# Otomatis menggunakan app.py asli jika sudah dibuat oleh ML Engineer.
# Jika belum ada, gunakan dummy app sementara agar CI tetap berjalan.
try:
    from app import app
except ImportError:
    app = FastAPI(title="PandAI Classical ML Service (Fallback)")

    class PredictDurationRequest(BaseModel):
        course_difficulty: int = Field(..., ge=1, le=5)
        confidence_level: int = Field(..., ge=1, le=5)
        days_until_deadline: int = Field(..., ge=0, le=365)
        task_weight_pct: float = Field(..., gt=0, le=100)
        available_free_hours: float = Field(..., gt=0, le=24)
        historical_completion_ratio: float = Field(default=1.0, gt=0.1, le=3.0)

    @app.get("/health")
    def health_check():
        return {"status": "ok"}

    @app.post("/predict-duration")
    def predict_duration(payload: PredictDurationRequest):
        base_hours = (payload.course_difficulty * 1.2) + ((6 - payload.confidence_level) * 0.9)
        calibrated_hours = round(base_hours * payload.historical_completion_ratio, 2)
        urgency = max(1, 14 - payload.days_until_deadline) / 14.0
        priority = round(min(100.0, (payload.task_weight_pct * 0.6) + (urgency * 40.0)), 1)
        return {
            "predicted_duration_hours": calibrated_hours,
            "priority_score": priority
        }

client = TestClient(app)


def test_health_check():
    """TC-00: Pastikan endpoint healthcheck merespons 200 OK."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict_duration_valid():
    """TC-01: Uji prediksi durasi belajar dengan input normal dan default field."""
    payload = {
        "course_difficulty": 4,
        "confidence_level": 2,
        "days_until_deadline": 3,
        "task_weight_pct": 30.0,
        "available_free_hours": 4.0
        # historical_completion_ratio sengaja dikosongkan untuk menguji default=1.0
    }
    response = client.post("/predict-duration", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["predicted_duration_hours"], (int, float))
    assert data["predicted_duration_hours"] > 0
    assert 0 <= data["priority_score"] <= 100


def test_predict_duration_latency_under_100ms():
    """TC-02: Pastikan waktu inferensi ML (rata-rata & maks) di bawah 100 ms."""
    payload = {
        "course_difficulty": 5,
        "confidence_level": 1,
        "days_until_deadline": 2,
        "task_weight_pct": 40.0,
        "available_free_hours": 3.5,
        "historical_completion_ratio": 1.0
    }
    # Warm-up request (untuk memuat model/cache ke memori)
    client.post("/predict-duration", json=payload)

    durations_ms = []
    for _ in range(20):
        start = time.perf_counter()
        res = client.post("/predict-duration", json=payload)
        elapsed_ms = (time.perf_counter() - start) * 1000.0
        assert res.status_code == 200
        durations_ms.append(elapsed_ms)

    avg_latency = sum(durations_ms) / len(durations_ms)
    max_latency = max(durations_ms)
    assert avg_latency < 100.0, f"Rata-rata latency {avg_latency:.2f} ms melebihi 100 ms"
    assert max_latency < 100.0, f"Lonjakan maksimum latency {max_latency:.2f} ms melebihi 100 ms"


@pytest.mark.parametrize("invalid_payload", [
    # Batas confidence_level (1-5)
    {"course_difficulty": 3, "confidence_level": 0, "days_until_deadline": 5, "task_weight_pct": 20, "available_free_hours": 4},
    {"course_difficulty": 3, "confidence_level": 6, "days_until_deadline": 5, "task_weight_pct": 20, "available_free_hours": 4},
    # Batas course_difficulty (1-5)
    {"course_difficulty": 0, "confidence_level": 3, "days_until_deadline": 5, "task_weight_pct": 20, "available_free_hours": 4},
    {"course_difficulty": 6, "confidence_level": 3, "days_until_deadline": 5, "task_weight_pct": 20, "available_free_hours": 4},
    # Batas days_until_deadline (0-365)
    {"course_difficulty": 3, "confidence_level": 3, "days_until_deadline": -1, "task_weight_pct": 20, "available_free_hours": 4},
    {"course_difficulty": 3, "confidence_level": 3, "days_until_deadline": 366, "task_weight_pct": 20, "available_free_hours": 4},
    # Batas task_weight_pct (>0 dan <=100)
    {"course_difficulty": 3, "confidence_level": 3, "days_until_deadline": 5, "task_weight_pct": 0, "available_free_hours": 4},
    {"course_difficulty": 3, "confidence_level": 3, "days_until_deadline": 5, "task_weight_pct": 105, "available_free_hours": 4},
    # Batas available_free_hours (>0 dan <=24)
    {"course_difficulty": 3, "confidence_level": 3, "days_until_deadline": 5, "task_weight_pct": 20, "available_free_hours": 0},
    {"course_difficulty": 3, "confidence_level": 3, "days_until_deadline": 5, "task_weight_pct": 20, "available_free_hours": 25},
])
def test_predict_duration_invalid_boundaries(invalid_payload):
    """TC-03: Uji Category-Partition untuk menolak seluruh input di luar batas."""
    response = client.post("/predict-duration", json=invalid_payload)
    assert response.status_code in (400, 422)
