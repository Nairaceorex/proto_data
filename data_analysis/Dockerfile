# data_analysis/Dockerfile
FROM python:3.10

WORKDIR /proto_data/data_analysis

COPY ./requirements.txt /proto_data/data_analysis/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /proto_data/data_analysis/requirements.txt

COPY ./main.py /proto_data/data_analysis/main.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
