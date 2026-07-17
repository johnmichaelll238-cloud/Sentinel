from app.storage.database import initialise_database
from app.collector.collector import collect_metrics

import time

COLLECTION_INTERVAL = 5


def main():
    initialise_database()

    print("Sentinel started...")

    while True:
        metrics = collect_metrics()
        print(metrics)
        time.sleep(COLLECTION_INTERVAL)


if __name__ == "__main__":
    main()