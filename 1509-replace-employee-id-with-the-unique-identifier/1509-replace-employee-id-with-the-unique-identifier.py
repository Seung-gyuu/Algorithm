import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    #  show the unique ID of each user, If a user does not have a unique ID replace just show null.
    df = pd.merge(employees, employee_uni, on='id', how="left")
    return df[["unique_id", "name"]]

    