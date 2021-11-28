from brownie import accounts, config, PriceFeedConsumer
#import os


def getAccount():
    #account = accounts.add(os.getenv("PRIVATE_KEY"))
    account = accounts.add(config["wallets"]["from_key"])
    print(account)


def deployPriceFeedConsumer():
    account = accounts[0]
    PFC = PriceFeedConsumer.deploy({"from_infura": account})
    ethPrice = PFC.getLatestPrice()
    print(ethPrice)


def main():
    # getAccount()
    deployPriceFeedConsumer()
