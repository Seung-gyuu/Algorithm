import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    #dropna() : drop missing val with nan and null
    return students.dropna(subset=["name"])