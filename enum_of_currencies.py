import asyncio
import datetime
from enum import Enum

from url_connection import url_connection

from settings import URL_BASE


date = datetime.date.today().strftime('%d.%m.%Y')

raw_server_response = asyncio.run(url_connection(URL_BASE + date))


def dict_of_currencies() -> dict:
    '''
    Creates a dict of avaliable currensies.
    '''
    result = {}
    for rsr in raw_server_response['exchangeRate']:
        result[rsr['currency']] = rsr['currency'].lower()
    return result


Currencies = Enum('Currencies', dict_of_currencies())

if __name__ == '__main__':
    print(Currencies.USD.value)
    print(any('USD' == item.name for item in Currencies))