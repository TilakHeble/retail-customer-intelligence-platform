"""
Project Configuration

Central location for all project paths.
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

INTERIM_DATA_DIR = DATA_DIR / "interim"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

DOCS_DIR = PROJECT_ROOT / "docs"

MODEL_DIR = PROJECT_ROOT / "models"

REPORT_DIR = PROJECT_ROOT / "reports"

LOG_DIR = PROJECT_ROOT / "logs"

# Automatically create required directories

for folder in [

    INTERIM_DATA_DIR,

    PROCESSED_DATA_DIR,

    DOCS_DIR,

    MODEL_DIR,

    REPORT_DIR,

    LOG_DIR

]:

    folder.mkdir(parents=True, exist_ok=True)
