import os

from app.service.security import is_valid_api_key


def test_is_valid_request_valid_API_key():
    assert is_valid_api_key(os.environ["BRAIN_API_KEY"]) is True


def test_is_valid_request_has_invalid_API_key():
    assert is_valid_api_key("INVALID") is False
