import io
import pathlib

from app.gcp.vision import label_image, ocr_image


def test_label_image():
    this_dir = pathlib.Path(__file__).parent
    sample_image_path = f"{this_dir}/../../samples/komakusa.jpg"

    with io.open(sample_image_path, "rb") as image_file:
        image = image_file.read()
    label = label_image(image)
    assert label["name"] == "Plant"


def test_ocr_image():
    this_dir = pathlib.Path(__file__).parent
    sample_image_path = f"{this_dir}/../../samples/note.jpg"

    with io.open(sample_image_path, "rb") as image_file:
        image = image_file.read()
    text_info = ocr_image(image)
    assert text_info["all_text"].startswith("This is") is True
    answers = text_info["answers"]
    assert len(answers) > 3
    assert answers[0]["text"] == "This"
