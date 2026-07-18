from app.ml.features import build_feature_matrix
from app.storage.database import get_latest_metric

from sklearn.ensemble import IsolationForest
import pandas as pd
#Implement class

class ModelManager:
    def __init__(self):
        self.training_limit = 100
        self.model = None

    def predict_latest(self):
        latest_metric = get_latest_metric()

        latest_df = pd.DataFrame([latest_metric])

        latest_df = latest_df[[
        "cpu_percent",
        "memory_percent",
        "memory_used",
        "memory_available",
        "disk_percent",
        ]]

        if self.model is None:
            return None

        prediction = self.model.predict(latest_df)

        return int(prediction[0])

    def retrain(self):
        self.model = train_model(self.training_limit)

#Training function

def train_model(
    limit: int = 100
    ):
    X = build_feature_matrix(limit)
    print(X.shape)
    model = IsolationForest(
    contamination=0.01,
    random_state=42
    )

    model.fit(X)
    
    return model

    
if __name__ == "__main__":
    manager = ModelManager()

    print(manager.predict_latest())