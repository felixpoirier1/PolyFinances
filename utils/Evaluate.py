import pandas as pd
from sklearn.metrics import mean_squared_error

def evaluate(pred_df: pd.DataFrame, test_path_csv: str) -> float:
    # Open test data
    test_df = pd.read_csv(test_path_csv)

    # Format data
    test_df['date'] = pd.to_datetime(test_df['date'], format='%Y-%m-%d')
    pred_df['date'] = pd.to_datetime(pred_df['date'], format='%Y-%m-%d')

    # Inner joint dataframe
    test_pred = test_df.merge(pred_df, on="date", how="inner")
    
    # Extract y true and y pred
    y_true = test_pred.FXUSDCAD_x.to_numpy()
    y_pred = test_pred.FXUSDCAD_y.to_numpy()

    mse = mean_squared_error(y_true, y_pred)
    print(f" Mean squared error: {mse}")

    # TODO: Add other metrics

    return mse
