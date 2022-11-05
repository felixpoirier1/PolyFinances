import pandas as pd

BASE_PATH = "data"

def split_and_save(df: pd.DataFrame, date_split='2022-05-01', filename_prefix=None, output_path='', keep_index=False):
    """ Simple function to split data set """
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

    # Split data
    """ Train data """
    train = df.loc[(df['date'] < date_split)]
    """ Test data """
    test = df.loc[(df['date'] >= date_split)]

    # Save Value
    if filename_prefix != None:
        train.to_csv(f"{BASE_PATH}/train/{output_path}/{filename_prefix}.csv", index=keep_index)
        test.to_csv(f"{BASE_PATH}/test/{output_path}/{filename_prefix}.csv", index=keep_index)
    
    return train, test
