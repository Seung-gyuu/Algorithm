import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # to find the rank of the scores( high - low ) / desc
    scores["rank"] = scores["score"].rank(ascending = False, method = "dense").astype("int")
    df =  scores[["score", "rank"]].sort_values(by = "score", ascending = False)
    return df

     