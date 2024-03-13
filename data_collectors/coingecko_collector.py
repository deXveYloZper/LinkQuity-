# /data_collectors/coingecko_collector.py

import requests

def fetch_trading_volume(coin_id='bitcoin'):
    """Fetches trading volume for a specified cryptocurrency from CoinGecko."""
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
    try:
        response = requests.get(url)
        data = response.json()
        trading_volume = data['market_data']['total_volume']['usd']
        return trading_volume
    except requests.RequestException as e:
        print(f"Failed to fetch data for {coin_id}: {e}")
        return None
