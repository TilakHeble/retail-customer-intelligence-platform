import pandas as pd


def remove_duplicates(df):

    return df.drop_duplicates()


def remove_empty_rows(df):

    return df.dropna(how="all")


def standardize_columns(df):

    df.columns = (

        df.columns

        .str.strip()

        .str.lower()

        .str.replace(" ","_")

    )

    return df
