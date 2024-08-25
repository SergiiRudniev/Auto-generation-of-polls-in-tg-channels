import logging
from typing import Tuple, List


def Parse(text: str) -> tuple[str, list[str], int]:
    logging.info(f"Parse Data: {text}")
    split = text.split("|")
    return str(split[0]), list(split[1].split(",")), int(split[2])