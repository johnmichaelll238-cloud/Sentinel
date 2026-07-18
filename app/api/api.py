from fastapi import FastAPI
from psutil import cpu_percent

from app.storage.database import (
    get_latest_metric,
    get_recent_metrics
)

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/metrics/latest")
def latest_metric():
    metric = get_latest_metric()
    return metric

@app.get("/metrics")
def recent_metrics(limit: int = 100):
    metrics = get_recent_metrics(limit)
    return metrics



@app.get("/anomaly")
def get_anomaly():
    metric = get_latest_metric()

    return {
        "prediction": metric["prediction"],
        "status": "normal" if metric["prediction"] == 1 else "anomaly",
        "timestamp": metric["timestamp"],
        "cpu_percent": metric["cpu_percent"],
        "memory_percent": metric["memory_percent"]
        }