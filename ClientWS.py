
import aiohttp
import asyncio


async def main():
    session = aiohttp.ClientSession()
    async with session.ws_connect('http://localhost:8080/websocket') as ws:

        await ws.send_str('Hi, i wanna to connect')

        async for msg in ws:
            print(f'Recieved from server:{msg}')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
