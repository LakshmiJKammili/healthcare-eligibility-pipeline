import pandas as pd

def read_partner_file(config):
    return pd.read_csv(
        config["file_path"],
        delimiter=config["delimiter"],
        dtype=str
    )
