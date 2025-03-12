import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # find employees who have the highest salary in each of the departments.
    merged_df = employee.merge(department, left_on = "departmentId", right_on = "id")
    merged_df["max"] = merged_df.groupby("departmentId")["salary"].transform("max")
    merged_df.rename(columns = { "name_x":"Employee", "name_y":"Department", "salary":"Salary"}, inplace = True)

    df = merged_df[merged_df["max"] == merged_df["Salary"]][["Department", "Employee", "Salary"]]
    return df
