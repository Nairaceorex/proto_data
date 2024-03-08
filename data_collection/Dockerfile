# data_collection/Dockerfile
FROM python:3.10

WORKDIR /proto_data/data_collection

COPY ./requirements.txt /proto_data/data_collection/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /proto_data/data_collection/requirements.txt

COPY ./main.py /proto_data/data_collection/main.py

COPY ./get_data_from_market /proto_data/data_collection/get_data_from_market
COPY ./get_data_from_market/Helpos /proto_data/data_collection/get_data_from_market/Helpos

ENV PYTHONPATH="/proto_data/data_collection/get_data_from_market:${PYTHONPATH}"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
