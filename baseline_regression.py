# %%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# %%

# Read in the data

def read_data(filename: str) -> pd.DataFrame:
    return pd.read_csv(f"data/dataset/{filename}.csv",
                       index_col=0, parse_dates=True)

df = read_data("FXUSDCAD")

# %%

# Create lag predictors for change rate

def create_lag_predictors(df: pd.DataFrame, n_lags: int) -> pd.DataFrame:
    for i in range(1, n_lags + 1):
        df[f"lag_{i}"] = df["change_rate"].shift(i)
    return df

df = create_lag_predictors(df, 5)