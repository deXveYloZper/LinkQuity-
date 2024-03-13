# main.py

from data_collectors.coingecko_collector import fetch_trading_volume

def main():
    bitcoin_volume = fetch_trading_volume()
    print(f"Bitcoin trading volume (USD): {bitcoin_volume}")

if __name__ == "__main__":
    main()
