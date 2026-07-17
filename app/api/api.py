from fastapi import FastAPI
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