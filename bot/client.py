import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

def create_client():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    
    # Use Binance Spot Testnet
    client = Client(api_key, api_secret)
    client.API_URL = 'https://testnet.binance.vision/api'
    return client
