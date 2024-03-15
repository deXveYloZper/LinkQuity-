# import requests

# def verify_coingecko_coin_ids(coin_symbols):
#     url = "https://api.coingecko.com/api/v3/coins/list"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         symbol_id_map = {coin['symbol'].upper(): coin['id'] for coin in data}
#         for symbol in coin_symbols:
#             print(f"{symbol}: {symbol_id_map.get(symbol.upper(), 'ID not found')}")
#     else:
#         print("Failed to fetch coin list from CoinGecko")

# # Example usage to verify IDs for specific coins
# coin_symbols = ['btc', 'eth', 'xrp', 'dot', 'ltc', 'link', 'xlm', 'uni']  # Add other symbols as needed
# verify_coingecko_coin_ids(coin_symbols)

import requests

def search_coingecko_coin_id(search_terms):
    url = "https://api.coingecko.com/api/v3/coins/list"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        found_coins = []

        # Search for coins by symbol or name
        for coin in data:
            if coin['symbol'].lower() in search_terms or coin['id'].lower() in search_terms:
                found_coins.append(coin)

        # Print found coins
        for coin in found_coins:
            print(f"{coin['id']} - {coin['symbol']}")

    else:
        print("Failed to fetch coin list from CoinGecko")

# Example usage
search_terms = ['btc', 'eth', 'xrp', 'dot', 'ltc', 'link', 'xlm', 'uni']  # Lowercase for matching
search_coingecko_coin_id(search_terms)
