import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    #DataFrame.isin(values) : Whether each element in the DataFrame is contained in values
    res = customers[~customers["id"].isin(orders["customerId"])][["name"]]
    return res.rename(columns = {"name": "Customers"})
    