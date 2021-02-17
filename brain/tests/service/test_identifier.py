import io
import pathlib

from app.service.identifier import _build_answer, identify


def test_identify():
    this_dir = pathlib.Path(__file__).parent
    sample_image_path = f"{this_dir}/../../samples/komakusa.jpg"

    with io.open(sample_image_path, "rb") as image_file:
        image = image_file.read()
    result = identify(image)
    assert len(result["answers"]) == 2


def test_build_answer_Plant():
    result = _build_answer({"name": "Plant", "score": 0.888})
    answers = result["answers"]
    assert len(answers) == 2
    assert answers[0]["speciesName"] == "タチツボスミレ"
    assert "respondentName" in answers[0]
    assert "respondentImageURL" in answers[0]
    assert "score" in answers[0]
    assert "message" in answers[0]


def test_build_answer_Fish():
    result = _build_answer({"name": "Fish", "score": 0.888})
    answers = result["answers"]
    assert len(answers) == 2
    assert answers[0]["speciesName"] == "カタクチイワシ"
    assert "respondentName" in answers[0]
    assert "respondentImageURL" in answers[0]
    assert "score" in answers[0]
    assert "message" in answers[0]


def test_build_answer_Unknown():
    result = _build_answer({"name": "SomethingUnknown", "score": 0.888})
    assert len(result["answers"]) == 0
    assert result["error"] == "Unknown target"
