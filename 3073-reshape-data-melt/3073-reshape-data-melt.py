import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    #pd.melt() : Unpivot a DataFrame from wide to long format
    res = pd.melt(report ,id_vars = "product", var_name = "quarter", value_name = "sales" )
    return res
    