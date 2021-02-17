from typing import Any, AnyStr, Dict, List

from ..gcp.vision import label_image


def identify(image: AnyStr) -> List[Any]:
    label = label_image(image)
    print(label)
    return _build_answer(label)


def _build_answer(label: Dict[str, Any]):
    name = label["name"]
    score = label["score"]
    if name == "Plant" or name == "Flower":
        return {
            "answers": [
                {
                    "speciesName": "タチツボスミレ",
                    "respondentName": "ミノリ",
                    "respondentImageURL": "https://example.com/charactors/minori/image.jpg",
                    "score": score,
                    "message": "たぶんタチツボスミレじゃないかな？",
                },
                {
                    "speciesName": "オオタチツボスミレ",
                    "respondentName": "ミノリ",
                    "respondentImageURL": "https://example.com/charactors/minori/image.jpg",
                    "score": score,
                    "message": "ひょっとしたらオオタチツボスミレかもしれない。",
                },
            ]
        }
    elif name == "Fish":
        return {
            "answers": [
                {
                    "speciesName": "カタクチイワシ",
                    "respondentName": "トト",
                    "respondentImageURL": "https://example.com/charactors/toto/image.jpg",
                    "score": score,
                    "message": "これはカタクチイワシだよ。",
                },
                {
                    "speciesName": "トウゴロウイワシ",
                    "respondentName": "トト",
                    "respondentImageURL": "https://example.com/charactors/toto/image.jpg",
                    "score": score,
                    "message": "これはトウゴロウイワシかもしれないねー。",
                },
            ]
        }
    return {"error": "Unknown target", "answers": []}
