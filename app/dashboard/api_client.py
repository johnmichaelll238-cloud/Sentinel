import requests

BASE_URL = "http://127.0.0.1:8000"

def get_latest_metrics(

)->dict:
    response = requests.get("http://127.0.0.1:8000/metrics/latest")
    response = response.json()

    return response

def get_recent_metrics(
    
)->list[dict]:
    history = requests.get(
    "http://127.0.0.1:8000/metrics?limit=100"
)

    history = history.json()
    return history