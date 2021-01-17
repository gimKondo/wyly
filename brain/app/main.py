"""
Application entry point
"""

from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()


@app.get("/")
async def index():
    """Sample API

    Returns:
        dict: Response
    """
    return {"message": "Hello world!"}


@app.post("/v1/identify")
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
                "message": "たぶんタチツボスミレじゃないかな？"
            },
            {
                "speciesName": "オオタチツボスミレ",
                "respondentName": "ミノリ",
                "respondentImageURL": "https://example.com/charactors/minori/image.jpg",
                "probability": 60,
                "message": "ひょっとしたらオオタチツボスミレかもしれない。"
            },
            {
                "speciesName": "カタクチイワシ",
                "respondentName": "トト",
                "respondentImageURL": "https://example.com/charactors/toto/image.jpg",
                "probability": 20,
                "message": "これはカタクチイワシだよ。"
            }
        ]
    }
