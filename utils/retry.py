import time
import requests
from utils.logging import get_logger

logger = get_logger()
def retry(func):
    def wrapper(*args, **kwargs):
        attempts = 0
        while attempts < 3:
            try:
                return func(*args, **kwargs)
            except requests.exceptions.RequestException as e:
                attempts += 1
                logger.warning(f"Retry {attempts} for {func.__name__}: {e}")
                time.sleep(2)
        raise Exception(f"Max retries exceeded for {func.__name__}")
    return wrapper