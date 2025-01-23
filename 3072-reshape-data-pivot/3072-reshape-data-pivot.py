import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    #df.pivot: Return reshaped DataFrame organized by given index / column values.
    pivot = weather.pivot(index="month" , columns = "city", values ="temperature")
    return pivot
    