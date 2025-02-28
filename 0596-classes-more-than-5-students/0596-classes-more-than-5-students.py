import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    # to find all the classes that have at least five students.
    df = courses.groupby("class")["student"].count().reset_index()
    df_filtered = df[df["student"] >= 5]
    return df_filtered[["class"]]
    