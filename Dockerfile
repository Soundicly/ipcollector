FROM python:3.11.4-slim

RUN apt-get update \
  && apt-get install -y --no-install-recommends git \
  && apt-get purge -y --auto-remove \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

ENV PORT=8000
ENV IP2LOCATION_DOWNLOAD_TOKEN="DOWNLOAD TOKEN FROM IP2LOCATION"

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
