from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

print("API KEY LOADED:", api_key)
print("API SECRET LOADED:", api_secret)

client = Client(api_key, api_secret, testnet=True)

client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"