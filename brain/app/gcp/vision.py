import io
import os
import pathlib
from functools import reduce
from typing import Any, Dict

from google.cloud import vision


def label_image(image_path: str) -> Dict[str, Any]:
    """label to image by Vision API

    Args:
        image_path (str): image path to label

    Raises:
        Exception: Something happens on calling Vision API

    Returns:
        Dict[str, Any]: label of image
    """
    this_dir = pathlib.Path(__file__).parent
    # TODO: set credential from ENV
    credential_json_path = f"{this_dir}/../credential/wyly-brain-dev.json"
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_json_path
    client = vision.ImageAnnotatorClient()

    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    response = client.label_detection(image=image)
    print(response)
    if response.error.message:
        raise Exception(response.error.message)

    labels = response.label_annotations
    best_label = reduce(lambda x, y: x if x.score > y.score else y, labels)

    return best_label
