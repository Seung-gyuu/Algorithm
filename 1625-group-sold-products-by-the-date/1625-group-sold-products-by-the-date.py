import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    # find for each date the number of different products sold and their names.
    df_count = activities.groupby("sell_date")["product"].nunique().reset_index()
    df_name = activities.groupby("sell_date")["product"].apply(lambda x : ",".join(sorted(set(x)))).reset_index()
    df = df_count.merge(df_name, on = "sell_date")
    return df.rename(columns = {"product_x":"num_sold", "product_y":"products"})

    