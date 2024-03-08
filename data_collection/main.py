from fastapi import FastAPI, Response
# importing os module for environment variables
import os
# importing necessary functions from dotenv library


from get_data_from_market.get_candles import get_candles_share

# loading variables from .env file


app = FastAPI()

fake_data = ["data1", "data2", "data3"]  # Предположим, это собранные данные


@app.get("/")
async def read_root():
    return {"message": "Data Collector Service"}


@app.get("/data")
async def get_data():
    return Response(get_candles_share().to_json(), media_type="application/json")
