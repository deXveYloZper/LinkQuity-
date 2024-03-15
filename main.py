# main.py

from data_collectors.crypto_data_collector import fetch_from_coingecko, fetch_all_cmc_volumes, CRYPTO_LIST

def main():
    """Fetches trading volumes for cryptocurrencies in CRYPTO_LIST and displays them."""
    # Fetch trading volumes from CoinMarketCap once before the loop
    cmc_volumes = fetch_all_cmc_volumes()

    for crypto in CRYPTO_LIST:
        cg_id, cmc_symbol = crypto
        cg_volume = fetch_from_coingecko(cg_id)

        # Use the pre-fetched CoinMarketCap data
        cmc_volume = cmc_volumes.get(cmc_symbol) if cmc_volumes else None

        print(f"\n{cg_id.capitalize()} Trading Volumes:")
        if cg_volume:
            print(f"CoinGecko: {cg_volume['trading_volume_usd']:,.2f} USD")
        else:
            print("CoinGecko: Data unavailable")

        # Now we directly access the trading volume for this cryptocurrency from the pre-fetched CoinMarketCap data
        if cmc_volume:
            print(f"CoinMarketCap: {cmc_volume:,.2f} USD")
        else:
            print("CoinMarketCap: Data unavailable")

if __name__ == "__main__":
    main()
