import requests
import json
from cfg import keys

class APIException(Exception):
    pass

class Converter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        if base == quote:
            raise APIException('Введены одинаковые валюты')
    
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')
    
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            amount=(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')
        
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        total_quote = json.loads(r.content)[keys[quote]]

        return total_quote

