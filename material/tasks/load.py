# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% tags=["soorgeon-imports"]
from sklearn import datasets
import matplotlib.pyplot as plt
import matplotlib as mpl
from pathlib import Path
import pickle
import pandas as pd

# %% tags=["parameters"]
upstream = None
product = None

# %% tags=["injected-parameters"]
# Parameters
sample = True
product = {
    "df": "/home/rpastorm/scipy/scipy-2022/material/output/load-df.parquet",
    "nb": "/home/rpastorm/scipy/scipy-2022/material/output/load.ipynb",
}


# %% [markdown]
# # Predicting median house value
#
# ## Load

# %%
plt.style.use('ggplot')
mpl.rcParams['figure.figsize'] = (12, 8)

# %%
ca_housing = datasets.fetch_california_housing(as_frame=True)
df = ca_housing['frame']

# %%
df.head()

# %% tags=["soorgeon-pickle"]
Path(product['df']).parent.mkdir(exist_ok=True, parents=True)
df.to_parquet(product['df'], index=False)

# %%
print(f'sample is {sample}')

# %%

def divide(x, y):
    return x / y

divide(1, 0)
