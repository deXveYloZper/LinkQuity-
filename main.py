# main.py

from data_collectors.coingecko_collector import fetch_trading_volume as fetch_cg_volume
from data_collectors.coinmarketcap_collector import fetch_cmc_trading_volume as fetch_cmc_volume

def main():
    print("Fetching trading volumes...")
    cg_volume = fetch_cg_volume('bitcoin')
    cmc_volume = fetch_cmc_volume('BTC')
    
    print(f"CoinGecko Bitcoin Trading Volume: {cg_volume} USD")
    print(f"CoinMarketCap Bitcoin Trading Volume: {cmc_volume} USD")

if __name__ == "__main__":
    main()
