import pandas as pd
import re

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:    
    users = users[users["mail"].apply(lambda x: bool(re.match(r"^[a-zA-Z][\w.-]*@leetcode\.com$", x)))]
    return users
