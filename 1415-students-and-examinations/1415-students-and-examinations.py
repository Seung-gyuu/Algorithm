import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    # to find the number of times each student attended each exam.
    stu_sub = students.merge(subjects, how = "cross")
    df = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')
    df1= stu_sub.merge(df, on = ["student_id","subject_name"], how="left")
    df1['attended_exams'] = df1['attended_exams'].fillna(0).astype(int)
    return df1.sort_values(by=["student_id","subject_name"])