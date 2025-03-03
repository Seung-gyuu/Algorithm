import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    # find managers with at least five direct reports.
    emp = employee.groupby("managerId")["id"].size().reset_index(name="count")
    emp = emp[emp["count"] >= 5]
    df = emp.merge(employee,left_on="managerId", right_on="id")[["name"]]
    return df
    