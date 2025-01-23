import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    #vertical_concat = pd.concat([df1, df2], axis=0)    # concatenating along rows
    #horizontal_concat = pd.concat([df1, df2], axis=1) # concatenating along columns
    return pd.concat([df1, df2], axis=0) 
    