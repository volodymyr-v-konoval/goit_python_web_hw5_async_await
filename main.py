import asyncio

import aiohttp

from typing import List, Optional, Dict, Any

from argument_parser import argument_parser
from date_list import date_list
from output_renderer import output_renderer
from settings import URL_BASE

dates = date_list(argument_parser())
currencies = ['EUR', 'USD'] 


async def url_connection(url: str) -> dict | None:
    '''
    Fetches a data dict from the remote server.
    '''
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    print(f"Error status: {response.status} for {url}.")
                    return None
        except aiohttp.ClientConnectorError as err:
            print(f'Connectio error: {url}', str(err))
            return None
        except aiohttp.ClientError as err:
            print(f"Client error: {url}", str(err))
            return None
        except asyncio.TimeoutError as err:
            print(f"Timeout error: {url}", str(err))
            return None
    

async def fetch_all_dates(list_of_dates: list, url: str) -> List[Optional[Dict[str, Any]]]:
    '''
    Fetches data from the provided URL for each date in the list_of_dates.
    '''
    tasks = []
    for date in list_of_dates:
        one_day_url = url + date
        tasks.append(url_connection(one_day_url))
    return await asyncio.gather(*tasks)


async def main():
    '''
    The main function which rules the show.
    '''
    currency_raw_list = await fetch_all_dates(dates, URL_BASE)
    result = []
    for currency_raw in currency_raw_list:
        if currency_raw:
            one_day_result = output_renderer(currencies, currency_raw)
            result.append(one_day_result)
        else:
            print("Skipping date due to connection issues.")
    print(result)

if __name__ == '__main__':
    asyncio.run(main())
