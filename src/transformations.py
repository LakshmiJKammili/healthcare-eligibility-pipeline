import pandas as pd
from datetime import datetime
import re


def apply_column_mapping(df, column_mapping):
    """
    Renames partner-specific columns to standard column names
    """
    return df.rename(columns=column_mapping)


def normalize_name(name):
    return name.title() if pd.notna(name) else None


def normalize_email(email):
    return email.lower() if pd.notna(email) else None


def normalize_dob(dob, date_format):
    try:
        return datetime.strptime(dob, date_format).strftime("%Y-%m-%d")
    except Exception:
        return None


def normalize_phone(phone):
    if pd.isna(phone):
        return None

    digits = re.sub(r"\D", "", phone)
    if len(digits) == 10:
        return f"{digits[0:3]}-{digits[3:6]}-{digits[6:]}"
    return None


def transform(df, config):
    df["first_name"] = df["first_name"].apply(normalize_name)
    df["last_name"] = df["last_name"].apply(normalize_name)
    df["email"] = df["email"].apply(normalize_email)
    df["dob"] = df["dob"].apply(lambda x: normalize_dob(x, config["date_format"]))
    df["phone"] = df["phone"].apply(normalize_phone)
    df["partner_code"] = config["partner_code"]

    return df
