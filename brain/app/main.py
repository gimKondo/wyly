"""
Application entry point
"""

from typing import List

from fastapi import FastAPI, File, Form, UploadFile
from pydantic import BaseModel

from .service.identifier import identify

app = FastAPI()


@app.get("/")
async def index():
    """Sample API

    Returns:
        dict: Response
    """
    return {"message": "Hello world!"}


class IdentifyAnswer(BaseModel):
    speciesName: str
    respondentName: str
    respondentImageURL: str
    score: int
    message: str


class IdentifyResponse(BaseModel):
    answers: List[IdentifyAnswer]


@app.post("/v1/identify", response_model=IdentifyResponse)
async def identify_v1(
    apiKey: str = Form(...),
    userId: str = Form(...),
    requestDate: str = Form(...),
    file: UploadFile = File(...),
):
    """API to identify species on photo

    Returns:
        dict: Response
    """
    req_data = {
        "apiKey": apiKey,
        "userId": userId,
        "requestDate": requestDate,
        "file_name": file.filename,
        "file_content_type": file.content_type,
    }
    print(req_data)
    return identify(file.file.read())
