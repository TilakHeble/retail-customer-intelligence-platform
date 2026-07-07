"""
==========================================================
Retail Customer Intelligence Platform

Configuration Module
==========================================================
"""

from pathlib import Path

# --------------------------------------------------------
# Project Root
# --------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# --------------------------------------------------------
# Data Directories
# --------------------------------------------------------

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

INTERIM_DATA_DIR = DATA_DIR / "interim"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

EXTERNAL_DATA_DIR = DATA_DIR / "external"

# --------------------------------------------------------
# Project Directories
# --------------------------------------------------------

SRC_DIR = PROJECT_ROOT / "src"

DOCS_DIR = PROJECT_ROOT / "docs"

REPORTS_DIR = PROJECT_ROOT / "reports"

MODELS_DIR = PROJECT_ROOT / "models"

LOGS_DIR = PROJECT_ROOT / "logs"

NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"

SQL_DIR = PROJECT_ROOT / "sql"

TESTS_DIR = PROJECT_ROOT / "tests"

DASHBOARD_DIR = PROJECT_ROOT / "dashboard"

# --------------------------------------------------------
# Automatically Create Directories
# --------------------------------------------------------

DIRECTORIES = [

    DATA_DIR,

    RAW_DATA_DIR,

    INTERIM_DATA_DIR,

    PROCESSED_DATA_DIR,

    EXTERNAL_DATA_DIR,

    DOCS_DIR,

    REPORTS_DIR,

    MODELS_DIR,

    LOGS_DIR,

    SQL_DIR,

    TESTS_DIR,

    DASHBOARD_DIR

]

for directory in DIRECTORIES:

    directory.mkdir(

        parents=True,

        exist_ok=True

    )

# --------------------------------------------------------
# Random Seed
# --------------------------------------------------------

RANDOM_STATE = 42

# --------------------------------------------------------
# Export Settings
# --------------------------------------------------------

CSV_ENCODING = "utf-8"

DATE_FORMAT = "%Y-%m-%d"

# --------------------------------------------------------
# Display Settings
# --------------------------------------------------------

PANDAS_DISPLAY_ROWS = 100

PANDAS_DISPLAY_COLUMNS = 100

PANDAS_FLOAT_FORMAT = "{:.2f}".format
