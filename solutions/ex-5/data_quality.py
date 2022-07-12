import pandas as pd


def no_nas(product):
    df = pd.read_parquet(product['df'])
    assert not df.MedHouseVal.isna().sum()
