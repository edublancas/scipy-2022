# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% tags=["soorgeon-imports"]
import seaborn as sns
from sklearn.linear_model import LinearRegression
from pathlib import Path
import pickle
import pandas as pd

# %% tags=["parameters"]
upstream = ['train-test-split']
product = None

# %% tags=["injected-parameters"]
# This cell was injected automatically based on your stated upstream dependencies (cell above) and pipeline.yaml preferences. It is temporary and will be removed when you save this notebook
upstream = {
    "train-test-split": {
        "y_test": "/Users/Edu/dev/scipy-2022/material/output/train-test-split-y_test.pkl",
        "X_train": "/Users/Edu/dev/scipy-2022/material/output/train-test-split-X_train.pkl",
        "y_train": "/Users/Edu/dev/scipy-2022/material/output/train-test-split-y_train.pkl",
        "X_test": "/Users/Edu/dev/scipy-2022/material/output/train-test-split-X_test.pkl",
        "nb": "/Users/Edu/dev/scipy-2022/material/output/train-test-split.ipynb",
    }
}
product = {"nb": "/Users/Edu/dev/scipy-2022/material/output/linear-regression.ipynb"}


# %% tags=["soorgeon-unpickle"]
X_test = pickle.loads(Path(upstream['train-test-split']['X_test']).read_bytes())
X_train = pickle.loads(Path(upstream['train-test-split']['X_train']).read_bytes())
y_test = pickle.loads(Path(upstream['train-test-split']['y_test']).read_bytes())
y_train = pickle.loads(Path(upstream['train-test-split']['y_train']).read_bytes())

# %% [markdown] tags=[]
# ## Linear regression

  # %% tags=[]
  # noqa

# %% tags=[]
lr = LinearRegression()

# %% tags=[]
lr.fit(X_train, y_train)

# %% tags=[]
y_pred = lr.predict(X_test)

# %% tags=[]
sns.scatterplot(x=y_test, y=y_pred)
