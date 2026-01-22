def validate(df):
    return df[df["external_id"].notna()]
