from brownie import PriceFeedConsumer, accounts, config, convert


def read_eth():
    # reads latest deployment of contract with -1
    eth_price = PriceFeedConsumer[-1]
    price = eth_price.getLatestPrice()
    price_formatted = price / (10**8)

    print(f"Current Ethereum price in USD: { price_formatted }")

    # output ETH value
    # return price_formatted


def main():
    read_eth()
