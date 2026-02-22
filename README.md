# **Machine Learning Development Platform with Docker & Jupyter**


This project provides a reproducible Machine Learning development environment using Docker.
It includes:

* A Jupyter Notebook container for interactive experimentation
* A Trainer container to automatically train a ML model
* Shared volumes to persist models, outputs, and notebooks
* Docker Compose to orchestrate everything easily

## **Project Structure**
```text
tarea_docker/
│
├── jupyter/
│   ├── Dockerfile
│   └── workspace/
│
├── trainer/
│   ├── Dockerfile
│   └── train.py
│
├── models/
├── output/
└── docker-compose.yml
```


## **Features**

* Fully reproducible Python ML environment
* Interactive Jupyter Notebook development
* Automatic model training script
* Shared persistent storage for:
  * trained models
  * plots and reports
  * notebooks
* Lightweight Docker images with optimized builds



## **How to run**

Check installation:
```bash
docker --version
docker compose version
```

Build the containers
```bash
docker compose build
```
Start the platform
```bash
docker compose up
```



## **Access Jupyter Notebook**

After running, open your browser:

http://localhost:8888

Copy the token from the terminal to log in.



## **Trainer Container**

The trainer container runs train.py, which:

* Generates synthetic data
* Trains a Linear Regression model
* Saves the model to models/model.pkl
* Saves a plot to output/training_plot.png

  

## **Output Files**

| File | Description |
|------|-------------|
| models/model.pkl | Trained ML model |
| output/training_plot.png | Training visualization |

## **Why Docker?**

Docker guarantees the same environment for everyone, avoiding problems like:

* Different OS (Windows / Mac / Linux)
* Different Python versions
* Missing libraries
* Deployment issues

This makes the project portable and reproducible.



## **Notes**

* Images are optimized using --no-cache-dir to reduce build time and memory usage

* Volumes allow sharing data between containers and the host system



## **Author**

Jiale Mao



## **License**

This project is licensed for academic use as part of the **Grado Ciencias de Datos** at **UPV**. It is intended for educational purposes and internal evaluation.
