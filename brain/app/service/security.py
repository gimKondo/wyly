import os


def is_valid_api_key(api_key: str) -> bool:
    """is valid API key or not
    Args:
        api_key (str)
    Returns:
        bool: is valid API key?
    """
    return api_key == os.environ["BRAIN_API_KEY"]
