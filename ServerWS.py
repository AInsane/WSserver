
import aiohttp
from aiohttp import web
import numpy as np


routes = web.RouteTableDef()
ws_responces={}

@routes.get('/')
async def hi_there(request):
    ws = ws_responces['ws1']
    await ws.send_str('ONE GET')
    return web.Response(text='HI Maaan')


@routes.get('/norm_distr')
async def norm_distr_generator(request):
    ws = ws_responces['ws1']

    mu, sigma = 0, 1
    s = np.random.normal(mu, sigma, 1000)
    # Really didn`t find how to get 95% of all numbers (think that they are between -2 and 2 ...)
    for i in s:
        if i >= -2 and i <= 2:
            print(i)
            await ws.send_str(f'Hey, i get number for you!: {i}')
    return web.Response(text='start workin`')


@routes.get('/websocket')
async def websocket_handler(request):
    print('WS connection started')
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    print('WS conn is ready')
    ws_responces['ws1'] = ws

    async for msg in ws:
        print(msg)
        if msg.type == aiohttp.WSMsgType.TEXT:
            print(msg.data)
            if msg.data == 'close':
                await ws.close()
            else:
                await ws.send_str(f'Your answer is :{msg.data}')

    print('Websocket connection closed')
    return ws






app = web.Application()
app.add_routes(routes)
web.run_app(app=app, port=8080)