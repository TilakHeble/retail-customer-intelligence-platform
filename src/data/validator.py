import pandas as pd

from src.logger import logger


def validate_dataset(df):

    report = {

        "rows": len(df),

        "columns": len(df.columns),

        "duplicates": df.duplicated().sum(),

        "missing_cells": df.isna().sum().sum(),

        "memory_mb":

        round(

            df.memory_usage(

                deep=True

            ).sum()

            /1024**2,

            2

        )

    }

    logger.info(report)

    return report
