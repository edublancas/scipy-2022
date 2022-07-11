# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.6
# ---

# %% tags=["soorgeon-imports"]
from sklearn.model_selection import train_test_split
from pathlib import Path
import pickle
import pandas as pd

# %% tags=["parameters"]
upstream = ['clean']
product = None

# %% tags=["soorgeon-unpickle"]
df = pd.read_parquet(upstream['clean']['df'])

# %% [markdown]
# ## Train test split

  # %%
  # noqa

# %%
X = df.drop('MedHouseVal', axis='columns')
y = df.MedHouseVal

# %%
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.33,
                                                    random_state=42)

# %% tags=["soorgeon-pickle"]
Path(product['X_test']).parent.mkdir(exist_ok=True, parents=True)
Path(product['X_test']).write_bytes(pickle.dumps(X_test))

Path(product['X_train']).parent.mkdir(exist_ok=True, parents=True)
Path(product['X_train']).write_bytes(pickle.dumps(X_train))

Path(product['y_test']).parent.mkdir(exist_ok=True, parents=True)
Path(product['y_test']).write_bytes(pickle.dumps(y_test))

Path(product['y_train']).parent.mkdir(exist_ok=True, parents=True)
Path(product['y_train']).write_bytes(pickle.dumps(y_train))
