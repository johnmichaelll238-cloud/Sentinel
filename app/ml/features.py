from app.storage.database import get_recent_metrics

import pandas as pd

def load_history(
    limit: int
):
    history = get_recent_metrics(limit)
    df = pd.DataFrame(history)

    return df
    
def build_feature_matrix(
    limit: int
):
    df = load_history(limit)
    df = df[[
    "cpu_percent",
    "memory_percent",
    "memory_used",
    "memory_available",
    "disk_percent",
    ]]

    return df
    