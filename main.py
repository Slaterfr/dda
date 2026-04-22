import requests as re
import pandas as pd


url = 'https://api.coingecko.com/api/v3/simple/price'

params = {
    'ids': 'bitcoin',
    'vs_currencies' : 'USD'
}

headers = {'x-cg-demo-api-key' : 'CG-eXMvH3mFCJg5w7BGd2kxWxhh'}


data = re.get(url='https://api.coingecko.com/api/v3/global', params=params)

print(data)

if data.status_code==200:
    response = data.json()
    #price = response['bitcoin']['usd']
    df = pd.DataFrame(response) 
    print(df)