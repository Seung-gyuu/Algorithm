import pandas as pd
import numpy as np

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    #to calculate the bonus of each employee
    #1) create employee["bonus"]
    #2) fill value - 100% of their salary if the ID of the employee is an odd number and the employee's name does not start with the character 'M'
    employees['bonus']= np.where((employees["employee_id"] % 2 != 0) & (~employees["name"].str.startswith("M")), employees["salary"] , 0)
    #ordered by employee_id & display employee_id, bonus
    return employees.sort_values("employee_id")[["employee_id", "bonus"]]
    