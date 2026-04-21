FROM python:3.12-slim

WORKDIR /app

COPY banquero.py .

ENTRYPOINT ["python", "banquero.py"]