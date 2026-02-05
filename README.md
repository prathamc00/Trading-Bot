Binance Futures Testnet Trading Bot (CLI)

This is a simple Python CLI application that places Market and Limit orders on Binance Futures Testnet (USDT-M).

The project is structured into separate modules for client setup, order logic, validation, logging, and CLI handling to keep the code clean and reusable.

Features

Place MARKET and LIMIT orders

Supports both BUY and SELL

CLI input using Typer

Input validation before API call

Logs all API requests and responses to a file

Basic error handling


File structure 

trading_bot/
│
├── bot/
│   ├── client.py          # Binance client setup
│   ├── orders.py          # Order placement logic
│   ├── validators.py      # CLI input validation
│   ├── logging_config.py  # Logging setup
│
├── cli.py                 # Entry point
├── .env                   # API keys
├── requirements.txt
└── README.md

Setup Instructions
1) Create Binance Futures Testnet Account

Register at Binance Futures Testnet and generate API keys.

Base URL used:

https://testnet.binancefuture.com

2) Add API keys

Create a .env file:

BINANCE_API_KEY=your_key
BINANCE_API_SECRET=your_secret

3) Install dependencies
pip install -r requirements.txt

How to Run

Run commands from the project root folder.

Market Order
python cli.py BTCUSDT BUY MARKET 0.001

Limit Order
python cli.py BTCUSDT SELL LIMIT 0.001 --price 60000

Logging

All order requests and responses are stored in:

trading.log


This helps in tracking API activity and debugging errors.

Notes

Quantity and price values must follow Binance lot size rules.

Only works on Binance Futures Testnet.

Designed as a small, modular CLI tool for clarity and easy extension.
