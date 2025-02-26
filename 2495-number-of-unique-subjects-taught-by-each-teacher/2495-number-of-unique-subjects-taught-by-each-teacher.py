import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    #  to calculate the number of unique subjects each teacher teaches in the university.
    df = teacher.groupby("teacher_id")["subject_id"].nunique().reset_index()
    df.rename(columns = {"subject_id" : "cnt"}, inplace =True)
    return df[["teacher_id", "cnt"]]
    