import pandas as pd
import numpy as np

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    cond = [
       accounts["income"] < 20000,
        (accounts["income"] >= 20000) & (accounts["income"] <= 50000),
        accounts["income"] > 50000
    ]
    category = ["Low Salary", "Average Salary", "High Salary"]
    accounts["category"] = np.select(cond, category)

    df = accounts.groupby("category").size().reset_index(name="accounts_count")
    #even if 0, need category -> reindex ( but to use reindex, need set_index first)
    df= df.set_index("category").reindex(category).fillna(0).reset_index()
    df["accounts_count"] = df["accounts_count"].astype(int)


    return df