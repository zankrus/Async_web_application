"""MAIN FILE for STAR WEB APP."""
import asyncio
from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response

from data_base_functons import try_make_db, insert_values, select_db
from service import input_validation

routes = web.RouteTableDef()


@routes.get('/')
async def hello(request: Request) -> Response:
    """ROUTE FOR / page."""
    print('GET Query incoming')
    res = await select_db()
    return web.Response(text=str(res))


@routes.post('/post')
async def post_to_db(request: Request) -> Response:
    """Behaviour for post request."""
    dict1 = await request.json()
    print(dict1)
    print('Post Query incoming ' + str(dict1))
    if input_validation(dict1):
        await insert_values(dict1["id"], dict1["status"])

    return web.Response(text=str(dict1))


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(try_make_db())
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)
    asyncio.get_event_loop().close()
