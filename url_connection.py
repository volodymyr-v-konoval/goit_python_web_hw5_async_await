import asyncio

import aiohttp




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
        