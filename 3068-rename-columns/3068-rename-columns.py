import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    #To rename index labels or col:  DataFrame.rename(mapper=None, *, index=None, columns=None, axis=None, copy=None, inplace=False, level=None, errors='ignore')[source]
    df = students.rename(columns={"id":"student_id", "first":"first_name", "last":"last_name","age":"age_in_years"})
    return df
    