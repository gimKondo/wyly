"""
Application entry point
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    """Sample API

    Returns:
        dict: Response
    """
    return {"message": "Hello world!"}
