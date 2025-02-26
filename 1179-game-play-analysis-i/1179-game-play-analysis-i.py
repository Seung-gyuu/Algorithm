import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    #  find the first login date for each player.
    act_df = activity[["player_id", "event_date"]]
    first_login = act_df.groupby("player_id")["event_date"].min().reset_index()
    return first_login.rename(columns = {"event_date": "first_login"})
