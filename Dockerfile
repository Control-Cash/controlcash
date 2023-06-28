FROM python:3-slim-bullseye

EXPOSE 8001
ENV PORT=8001

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

LABEL description="ControlCash"

# Install requirements
RUN apt-get update
RUN apt-get install -y pkg-config python3-dev default-libmysqlclient-dev build-essential

WORKDIR /code
COPY requirements.txt .

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

COPY controlCash/ .
COPY despesa/ .
COPY produto/ .
COPY venda/ .
COPY manage.py .

# Creates a non-root user and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers

RUN adduser --disabled-password --no-create-home appuser && chown -R appuser /code
ENV PATH="/code:$PATH"

USER appuser
