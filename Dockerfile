FROM python:3.9-alpine

EXPOSE 8000
ENV PORT=8000

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# instala dependencias do sistema para o mariadb
RUN apk add --no-cache musl-dev mariadb-connector-c-dev gcc mariadb-dev

# instala dependencias python
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /code

# RUN adduser -D -H appuser && chown -R appuser /code
# USER appuser

COPY controlCash/ .
COPY despesa/ .
COPY produto/ .
COPY venda/ .
COPY manage.py .


ENV PATH="/code:$PATH"

