"""
Application entry point
"""

from typing import List, Optional

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from pydantic import BaseModel

from .gcp.vision import ocr_image
from .service.identifier import identify
from .service.security import is_valid_api_key

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
    score: float
    message: str


class IdentifyResponse(BaseModel):
    answers: List[IdentifyAnswer]
    error: Optional[str]


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
    if not is_valid_api_key(apiKey):
        print(f"[[AUDIT]] invalid request. request:{req_data}")
        raise HTTPException(status_code=403, detail="Forbidden")
    print(req_data)
    return identify(file.file.read())


class OcrVertice(BaseModel):
    x: int
    y: int


class OcrRectangleVertices(BaseModel):
    left_upper: OcrVertice
    right_upper: OcrVertice
    right_bottom: OcrVertice
    left_bottom: OcrVertice


class OcrTextInfo(BaseModel):
    text: str
    vertices: OcrRectangleVertices


class OcrResponse(BaseModel):
    answers: List[OcrTextInfo]
    error: Optional[str]


@app.post("/v1/ocr", response_model=OcrResponse)
async def ocr_v1(
    apiKey: str = Form(...),
    file: UploadFile = File(...),
):
    """API to identify species on photo

    Returns:
        dict: Response
    """
    req_data = {
        "apiKey": apiKey,
        "file_name": file.filename,
        "file_content_type": file.content_type,
    }
    if not is_valid_api_key(apiKey):
        print(f"[[AUDIT]] invalid request. request:{req_data}")
        raise HTTPException(status_code=403, detail="Forbidden")
    print(req_data)
    texts = ocr_image(file.file.read())
    if len(texts) == 0:
        return {"error": "Not found any texts."}
    return {"answers": texts}
