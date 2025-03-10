import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    #  find the second highest distinct salary. If there is no second highest salary, return null.
    df = employee.drop_duplicates(subset="salary").sort_values(by = "salary")

    if len(df) < 2:
        return pd.DataFrame({"SecondHighestSalary" : [np.nan]})

    second = df.iloc[-2]["salary"]
    return pd.DataFrame({"SecondHighestSalary" :[second]})
    