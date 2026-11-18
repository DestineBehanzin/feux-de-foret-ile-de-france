FROM python:3.13-slim

WORKDIR /app

ENV PYTHONPATH=/app/src
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /app/requirements.txt

RUN python -m pip install \
    --no-cache-dir \
    --upgrade pip setuptools wheel

RUN python -m pip install \
    --no-cache-dir \
    -r /app/requirements.txt

COPY workspace.yaml /app/workspace.yaml
COPY src /app/src
COPY dbt /app/dbt