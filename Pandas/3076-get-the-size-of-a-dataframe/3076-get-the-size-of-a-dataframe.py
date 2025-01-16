import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    df = pd.DataFrame(players)
    result = list(df.shape)
    return  result
    