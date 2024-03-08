# data_visualization/Dockerfile
FROM python:3.9

WORKDIR /YS_D/data_visualization

COPY ./requirements.txt /YS_D/data_visualization/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /YS_D/data_visualization/requirements.txt

COPY ./main.py /YS_D/data_visualization/main.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]
