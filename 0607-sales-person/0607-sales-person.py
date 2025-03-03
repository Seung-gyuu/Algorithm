import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    #  find the names of all the salespersons who did not have any orders related to the company with the name "RED".
    if company[company["name"]== "RED"].empty:
        return sales_person[["name"]].drop_duplicates()

    red_id = company[company["name"]== "RED"]["com_id"].values[0]
    red_sales = orders[orders['com_id'] == red_id]['sales_id'].unique()

    sales = sales_person[["sales_id", "name"]]
    df = pd.merge(sales, orders , on="sales_id", how="left")

    return df[~df["sales_id"].isin(red_sales)][["name"]].drop_duplicates()
    