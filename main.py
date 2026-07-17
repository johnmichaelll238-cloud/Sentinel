from app.storage.database import initialise_database
from app.collector.collector import collect_metrics

initialise_database()

metrics = collect_metrics()

print(metrics)
print("The Lint is Clean 💎🥇🎯")