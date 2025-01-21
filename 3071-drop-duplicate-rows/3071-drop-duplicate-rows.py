import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    # DataFrame.drop_duplicates(subset=None, *, keep='first', inplace=False, ignore_index=False)[source]
    return customers.drop_duplicates(subset=['email'])
    