# Binance Futures Testnet Trading Bot

A Python CLI trading bot for Binance Futures Testnet that supports MARKET and LIMIT orders with logging, validation, and error handling.

## Features

- MARKET orders
- LIMIT orders
- BUY and SELL support
- Input validation
- Logging
- Error handling

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` file:

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
```

## Run MARKET Order

```bash
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

## Run LIMIT Order

```bash
python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```

## Logs

Logs are stored in:

```txt
logs/trading.log
```