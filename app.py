from fastapi import FastAPI
import platform
import socket

app = FastAPI()

@app.get("/")
def read_out():
    return {
        "message": "hello from inside a docker container",
        "python_version": platform.python_version(),
        "hostname": socket.gethostname()
    }