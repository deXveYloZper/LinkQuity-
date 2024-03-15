import requests
from utils.config_loader import get_api_key

# List of coins with their CoinGecko IDs and CoinMarketCap symbols
# Replace placeholders with the CORRECT VALUES based on service documentation
CRYPTO_LIST = [
    ('bitcoin', 'BTC'), 
    ('ethereum', 'ETH'),
    ('binancecoin', 'BNB'),  
    ('cardano', 'ADA'),
    ('solana', 'SOL'),
    ('ripple', 'XRP'), 
    ('polkadot', 'DOT'),
    ('litecoin', 'LTC'),
    ('chainlink', 'LINK'),
    ('stellar', 'XLM'),
    ('uniswap', 'UNI'),
]

def fetch_from_coingecko(coin_id):
    """Fetches trading volume and other data for a specified cryptocurrency from CoinGecko."""
    api_key = get_api_key('COINGECKO_API_KEY')
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        trading_volume_usd = data['market_data']['total_volume']['usd']
        current_price_usd = data['market_data']['current_price']['usd']
        market_cap_usd = data['market_data']['market_cap']['usd']
        
        return {
            'trading_volume_usd': trading_volume_usd,
            'current_price_usd': current_price_usd,
            'market_cap_usd': market_cap_usd
        }
    except Exception as e:
        print(f"Error fetching {coin_id} from CoinGecko: {e}")
        return None

# def fetch_from_coinmarketcap():
#     """Fetches trading volume from CoinMarketCap, handles potential errors.
#        Fetches a larger result set and filters client-side due to CoinMarketCap API limitations.
#     """
#     api_key = get_api_key('COINMARKETCAP_API_KEY')
#     headers = {
#         'Accepts': 'application/json',
#         'X-CMC_PRO_API_KEY': api_key,
#     }
#     parameters = {
#         'convert': 'USD', 
#         'limit': 500  # Fetch a larger number of listings 
#     }
#     url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

#     try:
#         response = requests.get(url, headers=headers, params=parameters)
#         response.raise_for_status()
#         data = response.json()

#         for coin_data in data['data']:
#             if coin_data['symbol'] in CRYPTO_LIST:  # Filter for coins you need
#                 return coin_data['quote']['USD']['volume_24h']

#         print("Error: Coin not found in CoinMarketCap listings")  # No match found
#         return None

#     except requests.RequestException as e:
#         print(f"Error fetching from CoinMarketCap: {e}")
#         return None

def fetch_all_cmc_volumes():
    """Fetches trading volumes for all cryptocurrencies from CoinMarketCap."""
    api_key = get_api_key('COINMARKETCAP_API_KEY')
    headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': api_key}
    parameters = {'convert': 'USD', 'limit': 200}  # Adjust 'limit' as necessary
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

    try:
        response = requests.get(url, headers=headers, params=parameters)
        response.raise_for_status()
        data = response.json()

        # Create a dictionary {symbol: volume_24h} for easier lookup
        volumes_by_symbol = {item['symbol']: item['quote']['USD']['volume_24h'] for item in data['data']}

        return volumes_by_symbol

    except requests.RequestException as e:
        print(f"Error fetching from CoinMarketCap: {e}")
        return None
