FROM python:3-slim-bullseye

EXPOSE 8001
ENV PORT=8001

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

LABEL description="Run Project"

# Install requirements
RUN apt-get update
RUN apt-get install -y pkg-config python3-dev default-libmysqlclient-dev build-essential

COPY .env .
COPY requirements.txt .

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

WORKDIR /code
ADD . /code

# Creates a non-root user and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers

RUN useradd appuser && chown -R appuser /code
USER appuser
