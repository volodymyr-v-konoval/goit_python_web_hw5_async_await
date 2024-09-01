import asyncio
import itertools

from argument_parser import check_currencies, check_range
from date_list import date_list
from main import fetch_all_dates
from output_renderer import output_renderer
from settings import URL_BASE, CURRENCIES



def web_argument_parser(web_args: str) -> list:
    '''
    Parses the web line input.
    '''

    list_arg = web_args.split()[1:]

    if list_arg and check_range(list_arg[0]):
        number_of_days = int(list_arg[0])
        arg_currencies = list_arg[1:]
    else: 
        number_of_days = 1
        arg_currencies = list_arg
    currencies = check_currencies(list(dict.fromkeys(itertools.chain(CURRENCIES, arg_currencies))))
    return [number_of_days, currencies]






async def exchange(web_arg: str) -> str:
    if web_arg.split()[0] != 'exchange':
        return web_arg
    else:
        number_of_days, currencies = web_argument_parser(web_arg)
        dates = date_list(number_of_days)
        currency_raw_list = await fetch_all_dates(dates, URL_BASE)
        result = []
        for currency_raw in currency_raw_list:
            if currency_raw:
                one_day_result = output_renderer(currencies, currency_raw)
                result.append(one_day_result)
            else:
                print("Skipping date due to connection issues.")
        return(result)
        
   
if __name__ == '__main__':
    asyncio.run(exchange('exchange 2 chf'))
