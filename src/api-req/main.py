import requests
import pandas as pd
from token import token


def setKeys():
    headers = {"Authorization": "Bearer " + token}
    r = requests.get(base_url + "users", headers=headers)
    dataframe = pd.DataFrame(columns=r.json()["data"][0].keys())
    return dataframe


records_df = setKeys()
