# FastAPI Docker Demo

A simple FastAPI application containerized using Docker.

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Docker

## Docker Image

Docker Hub Image:

gayudangi/fastapi-app:v1

## Run with Docker

Pull the Docker image:

```bash
docker pull gayudangi/fastapi-app:v1

docker run -d --name fastapi-demo -p 8001:8000 gayudangi/fastapi-app:v1
