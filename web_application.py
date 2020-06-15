import asyncio
import time
import requests

from aiohttp import web
from aiohttp.abc import BaseRequest

from data_base_functons import try_make_db, insert_values, select_db
from service import status_randomizer, id_randomizer

routes = web.RouteTableDef()

@routes.get('/')
async def hello(request):
    print('GET Query incoming')
    print(request)
    res = await select_db()
    return web.Response(text=str(res))




@routes.post('/post')
async def post_to_db(request):
    dict1 = await request.json()
    print(dict1)
    print('Post Query incoming')
    # await insert_values(dict1[''])
    return web.Response(text=str(dict1))
    # List of all current deliveries



asyncio.get_event_loop().run_until_complete(try_make_db())
app = web.Application()
app.add_routes(routes)
web.run_app(app)
