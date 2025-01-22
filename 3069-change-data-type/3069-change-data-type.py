import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    # To convert argument to a numeric type
    # 1) pandas.to_numeric(arg, errors='raise', downcast=None, dtype_backend=<no_default>)[source]
    # 2) df['Column1'] = df['Column1'].map(int)
    # 3) df['Column1'] = df['Column1'].apply(lambda x: int(x))
    students["grade"] = students["grade"].map(int)
    return students
    