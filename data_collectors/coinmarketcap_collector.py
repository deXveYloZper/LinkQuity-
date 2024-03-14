# data_collectors/coinmarketcap_collector.py

import requests
from utils.config_loader import get_api_key

def fetch_cmc_trading_volume(coin_symbol='BTC'):
    """Fetches trading volume for a specified cryptocurrency from CoinMarketCap."""
    api_key = get_api_key('COINMARKETCAP_API_KEY')
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    parameters = {
        'symbol': coin_symbol,
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }
    
    try:
        response = requests.get(url, headers=headers, params=parameters)
        response.raise_for_status()  # Check for HTTP request errors
        data = response.json()
        trading_volume = data['data'][coin_symbol]['quote']['USD']['volume_24h']
        return trading_volume
    except requests.RequestException as e:
        print(f"Error fetching data from CoinMarketCap: {e}")
        return None
