from app.storage.database import initialise_database, update_latest_prediction
from app.collector.collector import collect_metrics
from app.ml.anomaly import ModelManager

import time

COLLECTION_INTERVAL = 5

def main():
    initialise_database()

    model_manager = ModelManager()

    collection_count = 0

    train_after_interval = 5

    print("Sentinel started...")

    while True:
        metrics = collect_metrics()
        
        if model_manager.model is not None:
            prediction = model_manager.predict_latest()
            update_latest_prediction(prediction) 
            print(prediction)       
        
        print(metrics)

        collection_count += 1

        if collection_count >= train_after_interval:
            model_manager.retrain()
            collection_count = 0
        
        time.sleep(COLLECTION_INTERVAL)


if __name__ == "__main__":
    main()