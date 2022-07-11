# content of data_quality.py
import pandas as pd

def no_nas(product):
    df = pd.read_parquet(product['df'])

    # raise ValueError("Forcing error")
    assert not df.MedHouseVal.isna().sum()