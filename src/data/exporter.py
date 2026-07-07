from src.config import INTERIM_DATA_DIR


def save_dataset(

    df,

    filename

):

    df.to_csv(

        INTERIM_DATA_DIR /

        filename,

        index=False

    )
