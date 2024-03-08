# data_visualization/Dockerfile
FROM python:3.10

WORKDIR /proto_data/data_visualization

COPY ./requirements.txt /proto_data/data_visualization/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /proto_data/data_visualization/requirements.txt

COPY ./main.py /proto_data/data_visualization/main.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]
