import json
import yfinance

from conn.aiohttp_wrapper import AioHttpClient
from utils.func import get_path

api_binance_url = "https://api.binance.com/api/v3/ticker/price?symbol="


async def result_stock(source: str, stock_name: str, **kwargs) -> any:
    if source == 'yahoo':
        if get_path(kwargs, 'information') is not None:
            return None
        else:
            return result_yahoo_stock(stock_name, get_path(kwargs, 'information'))
    else:
        return None


async def result_yahoo_stock(stock_name: str, information: str) -> any:
    if not information:
        information = 'info'
    try:
        return eval(f'yfinance.Ticker("{stock_name}").{information}')
    except Exception as e:
        print(e)
        return e


async def result_binance_crypto(pair_name: str) -> any:
    try:
        request_result = await AioHttpClient.get(url=api_binance_url + pair_name, headers={
            'Content-Type': 'application/json'})
        return request_result
    except Exception as e:
        print(e)
        return e
