import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    # to calculate the total time in minutes spent by each employee on each day at the office.  
    # The time spent in the office for a single entry is out_time - in_time.
    employees["total_time"]  = employees["out_time"] - employees["in_time"]
    employees = employees.groupby(["emp_id","event_day"])["total_time"].sum().reset_index()
    employees.rename(columns = {"event_day":"day"}, inplace=True)
    return employees[["day", "emp_id", "total_time"]]
    