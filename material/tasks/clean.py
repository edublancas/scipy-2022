# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.0
# ---

# %% tags=["soorgeon-imports"]
import seaborn as sns
from pathlib import Path
import pickle
import pandas as pd

# %% tags=["parameters"]
upstream = ['load']
product = None

# %% tags=["soorgeon-unpickle"]
df = pd.read_parquet(upstream['load']['df'])

# %% [markdown]
# ## Clean

# %%
sns.histplot(df.HouseAge)

# %%
# let's say we're only interested in newer homes, so we define this filtering
# rule
df = df[df.HouseAge <= 30]

# %%
sns.histplot(x=df.AveBedrms)

# %%
sns.boxplot(x=df.AveBedrms)

# %%
# let's also remove big houses
df = df[df.AveBedrms <= 4]

# %%
# distribution of our target variable
sns.histplot(df.MedHouseVal)

# %% tags=["soorgeon-pickle"]
Path(product['df']).parent.mkdir(exist_ok=True, parents=True)
df.to_parquet(product['df'], index=False)
