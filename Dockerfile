FROM python:3.9

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2 pyarrow wheel

WORKDIR /app
COPY ingest_data.py ingest_data.py
#COPY ingest_taxi_zone_data.py ingest_taxi_zone_data.py

ENTRYPOINT ["python", "ingest_data.py"]
