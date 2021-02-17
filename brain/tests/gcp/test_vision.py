import pathlib

from app.gcp.vision import label_image


def test_label_image():
    this_dir = pathlib.Path(__file__).parent
    sample_image_path = f"{this_dir}/../../samples/komakusa.jpg"
    label = label_image(sample_image_path)
    assert label.description == "Plant"
