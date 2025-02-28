import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # find the customer_number for the customer who has placed the largest number of orders.
    df = orders.groupby("customer_number")["order_number"].count().reset_index()
    max_order = df["order_number"].max()
    return df[df["order_number"] == max_order][["customer_number"]]