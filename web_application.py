import asyncio
import time
import requests

from aiohttp import web

from data_base_functons import try_make_db, insert_values
from service import status_randomizer, id_randomizer

routes = web.RouteTableDef()

@routes.get('/')
async def hello(request):
    print('Get Query incoming')
    return web.Response(text=str({status_randomizer(): id_randomizer()}))
    # List of all current deliveries



@routes.post('/post')
async def post_to_db(request):

    print('Post Query incoming')
    return web.Response(text="Hello, world")
    # List of all current deliveries


asyncio.get_event_loop().run_until_complete(try_make_db())
asyncio.get_event_loop().run_until_complete(insert_values('2', '4'))
app = web.Application()
app.add_routes(routes)
web.run_app(app)
