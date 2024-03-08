from fastapi import FastAPI

app = FastAPI()

fake_data = ["data1", "data2", "data3"]  # Предположим, это собранные данные

@app.get("/")
async def read_root():
    return {"message": "Data Collector Service"}

@app.get("/data")
async def get_data():
    return {"data": fake_data}

