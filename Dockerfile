FROM python:3

LABEL authors="gamid"

WORKDIR /app

COPY /requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
