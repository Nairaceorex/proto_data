from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Data Visualization Service"}

# Здесь можно добавить код для визуализации данных

