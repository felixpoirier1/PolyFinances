# %%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# %%

# Read in the data

def read_data(filename: str) -> pd.DataFrame:
    return pd.read_csv(f"data/dataset/{filename}.csv",
                       index_col=0, parse_dates=True)

df = read_data("usdcad")
print(df.head())

# %%

# Create lag predictors for change rate

def create_lag_predictors(df: pd.DataFrame, n_lags: int, col_to_lag: str) -> pd.DataFrame:
    for i in range(1, n_lags + 1):
        df[f"{col_to_lag}_lag_{i}"] = df[col_to_lag].shift(i)
    return df

df = create_lag_predictors(df, 10, "DEXCAUS")


# %%

# compute percentage change for all columns

def compute_pct_change(df: pd.DataFrame) -> pd.DataFrame:
    df_pct = df[df.columns[1:]].pct_change()
    df_concat = pd.concat([df[df.columns[0]], df_pct], axis=1)

    return df_concat

df = compute_pct_change(df)

# %%

df.dropna(inplace=True)

# %%
# Drop all rows with NaN values

X = df[df.columns[1:]]
y = df[df.columns[0]]

print(X)

#%%


model = LinearRegression()
model.fit(X, y)
print(model.score(X, y))


# %%









