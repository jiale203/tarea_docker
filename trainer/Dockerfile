FROM python:3.10-slim

WORKDIR /trainer

RUN apt-get update && apt-get install -y \
    build-essential python3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    numpy pandas scikit-learn matplotlib joblib


COPY train.py .

CMD ["python", "train.py"]
