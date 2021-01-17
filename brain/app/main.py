"""
Application entry point
"""

from typing import List

from fastapi import FastAPI, File, Form, UploadFile
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def index():
    """Sample API

    Returns:
        dict: Response
    """
    return {"message": "Hello world!"}


class IdentifyResponse(BaseModel):
    speciesName: str
    respondentName: str
    respondentImageURL: str
    probability: int
    message: str


@app.post("/v1/identify", response_model=List[IdentifyResponse])
async def identify(
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
    return {
        "answers": [
            {
                "speciesName": "タチツボスミレ",
                "respondentName": "ミノリ",
                "respondentImageURL": "https://example.com/charactors/minori/image.jpg",
                "probability": 80,
                "message": "たぶんタチツボスミレじゃないかな？",
            },
            {
                "speciesName": "オオタチツボスミレ",
                "respondentName": "ミノリ",
                "respondentImageURL": "https://example.com/charactors/minori/image.jpg",
                "probability": 60,
                "message": "ひょっとしたらオオタチツボスミレかもしれない。",
            },
            {
                "speciesName": "カタクチイワシ",
                "respondentName": "トト",
                "respondentImageURL": "https://example.com/charactors/toto/image.jpg",
                "probability": 20,
                "message": "これはカタクチイワシだよ。",
            },
        ]
    }
