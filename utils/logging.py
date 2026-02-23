import logging
import os
from datetime import datetime

def get_logger():
    os.makedirs("reports", exist_ok=True)

    log_file = f"reports/test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

    logger = logging.getLogger("API")
    logger.setLevel(logging.INFO)

    # Clear old handlers (VERY IMPORTANT)
    if logger.hasHandlers():
        logger.handlers.clear()

    file_handler = logging.FileHandler(log_file, mode="a")
    file_formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    file_handler.setFormatter(file_formatter)

    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )
    console_handler.setFormatter(console_formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger