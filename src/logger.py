import logging

from pathlib import Path

from src.config import LOG_DIR

LOG_FILE = LOG_DIR / "project.log"

logging.basicConfig(

    level=logging.INFO,

    format="%(asctime)s | %(levelname)s | %(message)s",

    handlers=[

        logging.FileHandler(LOG_FILE),

        logging.StreamHandler()

    ]

)

logger = logging.getLogger(__name__)
