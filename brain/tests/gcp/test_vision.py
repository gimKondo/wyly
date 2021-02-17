import io
import pathlib

from app.gcp.vision import label_image


def test_label_image():
    this_dir = pathlib.Path(__file__).parent
    sample_image_path = f"{this_dir}/../../samples/komakusa.jpg"

    with io.open(sample_image_path, "rb") as image_file:
        image = image_file.read()
    label = label_image(image)
    assert label["name"] == "Plant"
