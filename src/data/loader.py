from pathlib import Path

import pandas as pd

from src.config import RAW_DATA_DIR

from src.logger import logger


def load_all_data():

    """
    Load every CSV file
    from the raw directory.

    Returns
    -------

    dict
    """

    datasets = {}

    csv_files = sorted(

        RAW_DATA_DIR.glob("*.csv")

    )

    logger.info(

        f"Found {len(csv_files)} datasets."

    )

    for file in csv_files:

        df = pd.read_csv(file)

        datasets[file.stem] = df

        logger.info(

            f"{file.name} "

            f"{df.shape[0]} rows "

            f"{df.shape[1]} columns"

        )

    return datasets
