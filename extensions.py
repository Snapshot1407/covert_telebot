import requests
import json

from Constants import VALUES

class APIException(Exception):
    pass

class Convertor():
    def get_price(base, symbols, amount):
        try:
            base_key = VALUES[base.lower()]
        except KeyError:
            raise APIException(f"Валюта {base} не найдена!")

        try:
            sym_key = VALUES[symbols.lower()]
        except KeyError:
            raise APIException(f"Валюта {symbols} не найдена!")

        if base_key == sym_key:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}!')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}!')
        r = requests.get(f"https://api.exchangerate.host/latest?base={base_key}&symbols={sym_key}")

        text = json.loads(r.content)
        new_price = text['rates'][sym_key] * float(amount)
        new_price = round(new_price, 3)
        message = f"Цена {amount} {base} в {symbols} : {new_price}"
        return message
