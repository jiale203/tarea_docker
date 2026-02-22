FROM python:3.10-slim



ENV DEBIAN_FRONTEND=noninteractive



RUN apt-get update && apt-get install -y \

    build-essential python3-dev \

    && rm -rf /var/lib/apt/lists/*



WORKDIR /workspace


RUN pip install --no-cache-dir \
    numpy pandas scikit-learn jupyter matplotlib joblib


EXPOSE 8888



CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]
