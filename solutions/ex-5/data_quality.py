import pandas as pd


def no_nas(product):
    df = pd.read_parquet(product['df'])
    raise ValueError('breaking things on purpose')
    assert not df.MedHouseVal.isna().sum()
