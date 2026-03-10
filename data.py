import pandas as pd
import requests

def get_pedestrian_data():
    url = "https://data.melbourne.vic.gov.au/api/explore/v2.1/catalog/datasets/pedestrian-counting-system-monthly-counts-per-hour/records"
    params = {"limit": 100}
    response = requests.get(url, params=params)
    data = response.json()
    df = pd.DataFrame(data["results"])
    return df

if __name__ == "__main__":
    df = get_pedestrian_data()
    print(df.head())
    print(f"Columns: {df.columns.tolist()}")    