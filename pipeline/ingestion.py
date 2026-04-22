import requests
import pandas as pd
from ..config import Config
from datetime import date, datetime
from pathlib import Path
import json
import os 


class Ingestion:

    HEADERS = {'x-cg-demo-api-key': Config.GEKO_KEY}

    @staticmethod
    def get_marked_data(coin : str = None):
        """
        Fetch market data for a specified coin using the CoinGecko API.
        
        Args:
            coin (str): The coin identifier (e.g., 'bitcoin')
            
        Returns:
            dict: JSON response from the API
        """
        params = {
            'ids': coin,
            'vs_currency': 'USD',
            'order': 'market_cap_desc',
            'per_page': 10
        }
        
        url = f'https://api.coingecko.com/api/v3/coins/markets'
        response = requests.get(url=url, params=params, headers=Ingestion.HEADERS)
        if response.status_code !=200:
            raise Exception(f"API Error")
        data = response.json()

        #validations and saving records of raw data
        Ingestion.validate_raw(data)
        Ingestion.save_raw(data)
        
        #print(data)

        return data
    
    @staticmethod
    def validate_raw(data):
        if not isinstance(data, list):
            raise ValueError("API did not reyutn a list.")

        if len(data)==0:
            raise ValueError("Empty API response")


        sample = data[0]

        required_keys = ["id","current_price", "market_cap", "total_volume", "last_updated"]

        missing = [k for k in required_keys if k not in sample]
        if missing:
            raise ValueError(f"API Missing keys: {missing}")
        
    @staticmethod
    def save_raw(data):
        now = datetime.now()

        date_path = now.strftime("%y-%m-%d")
        time_path = now.strftime("%H-%M-%S")

        path = f"data/raw{date_path}"

        os.makedirs(path, exist_ok=True)

        file_path = f"{path}/coins_{time_path}.json"

        with open(file_path, "w") as f:
            json.dump(data, f)


if __name__ == '__main__':
    Ingestion.get_marked_data()
