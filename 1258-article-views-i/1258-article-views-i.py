import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    res = views[views["author_id"]==views["viewer_id"]][["author_id"]].drop_duplicates(subset="author_id", keep="first")
    res = res.rename(columns={"author_id" : "id"}).sort_values(by='id', ascending=True)
    return res