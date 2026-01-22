
from config import PARTNER_CONFIG
from ingestion import read_partner_file
from transformations import apply_column_mapping, transform
from validation import validate
import pandas as pd


def process_partner(partner_name):
    config = PARTNER_CONFIG[partner_name]

    df = read_partner_file(config)
    df = apply_column_mapping(df, config["column_mapping"])
    df = transform(df, config)
    df = validate(df)

    return df[
        [
            "external_id",
            "first_name",
            "last_name",
            "dob",
            "email",
            "phone",
            "partner_code",
        ]
    ]


def main():
    all_dfs = []

    for partner_name in PARTNER_CONFIG.keys():
        partner_df = process_partner(partner_name)
        all_dfs.append(partner_df)

    unified_df = pd.concat(all_dfs, ignore_index=True)
    unified_df.to_csv("output/unified_eligibility.csv", index=False)


if __name__ == "__main__":
    main()
