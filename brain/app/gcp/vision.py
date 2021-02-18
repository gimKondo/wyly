from functools import reduce
from typing import Any, AnyStr, Dict

from google.cloud import vision


def label_image(image: AnyStr) -> Dict[str, Any]:
    """label to image by Vision API

    Args:
        image (AnyStr): image data to label

    Raises:
        Exception: Something happens on calling Vision API

    Returns:
        Dict[str, Any]: label of image
    """
    client = vision.ImageAnnotatorClient()

    vision_image = vision.Image(content=image)

    response = client.label_detection(image=vision_image)
    print(response)
    if response.error.message:
        raise Exception(response.error.message)

    labels = response.label_annotations
    best_label = reduce(lambda x, y: x if x.score > y.score else y, labels)

    return {
        "name": best_label.description,
        "score": best_label.score,
    }


def ocr_image(image: AnyStr) -> Dict[str, Any]:
    """OCR image by Vision API

    Args:
        image (AnyStr): image data to label

    Raises:
        Exception: Something happens on calling Vision API

    Returns:
        Dict[str, Any]: detected texts info
    """
    client = vision.ImageAnnotatorClient()

    vision_image = vision.Image(content=image)

    response = client.text_detection(image=vision_image)
    # print(response)
    if response.error.message:
        raise Exception(response.error.message)

    if len(response.text_annotations) < 2:
        return {"error": ""}

    texts = []
    for annotation in response.text_annotations[1:]:
        vertices = annotation.bounding_poly.vertices
        print("----------------------")
        print(annotation.description)
        print(annotation.bounding_poly)
        print("----------------------")
        text_data = {
            "text": annotation.description,
            "vertices": {
                "left_upper": {"x": vertices[0].x, "y": vertices[0].y},
                "right_upper": {"x": vertices[1].x, "y": vertices[1].y},
                "right_bottom": {"x": vertices[2].x, "y": vertices[2].y},
                "left_bottom": {"x": vertices[3].x, "y": vertices[3].y},
            },
        }
        texts.append(text_data)

    return {"all_text": response.text_annotations[0].description, "answers": texts}
