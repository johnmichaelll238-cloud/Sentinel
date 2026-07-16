from datetime import datetime

from app.collector.cpu import get_cpu_metrics
from app.storage.database import insert_metrics


def collect_metrics(

)->dict:    
    metrics = get_cpu_metrics()

    metrics["timestamp"] = datetime.now().isoformat()

    insert_metrics(metrics)

    return metrics
