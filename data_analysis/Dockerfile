# data_analysis/Dockerfile
FROM python:3.9

WORKDIR /YS_D/data_analysis

COPY ./requirements.txt /YS_D/data_analysis/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /YS_D/data_analysis/requirements.txt

COPY ./main.py /YS_D/data_analysis/main.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
