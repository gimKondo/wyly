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

    return best_label
