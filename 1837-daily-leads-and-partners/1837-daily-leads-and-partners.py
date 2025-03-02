import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    # For each date_id and make_name, find the number of distinct lead_id's and distinct partner_id's.
    df = daily_sales.groupby(["date_id", "make_name"]).agg({
        "lead_id" : "nunique",
        "partner_id" : "nunique"
    }).reset_index()
    df.rename(columns = {"lead_id" : "unique_leads", "partner_id": "unique_partners"}, inplace=True)
    return df
    