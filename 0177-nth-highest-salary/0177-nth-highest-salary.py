import numpy as np
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    sorted = employee.drop_duplicates(subset="salary").sort_values(by = "salary", ascending = False).reset_index()
    if N <= 0 or N > len(sorted):
        return pd.DataFrame([np.nan], columns=[f"getNthHighestSalary({N})"])
    n_sal = sorted.iloc[N-1]["salary"]
    

    df = sorted[sorted["salary"] == n_sal][["salary"]]  
    df = df.rename(columns = {"salary" :  f"getNthHighestSalary({N})"})
    return df