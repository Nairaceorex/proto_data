# data_collection/Dockerfile
FROM python:3.9

WORKDIR /YS_D/data_collection

COPY ./requirements.txt /YS_D/data_collection/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /YS_D/data_collection/requirements.txt

COPY ./main.py /YS_D/data_collection/main.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
