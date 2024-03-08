from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Data Analyzer Service"}

@app.get("/analyze")
async def analyze_data():
    

    # URL микросервиса data_collector, указанный в docker-compose.yml
    data_collector_url = "http://data_collection:8000"

    # Пример запроса GET к data_collector
    response = requests.get(data_collector_url + "/data")
    data = response.json()
    # Здесь должен быть код анализа данных
    return {"result": data}

