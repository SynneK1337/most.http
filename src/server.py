from aiohttp import web
from scrap import Scrap

async def handle(request):
    state = Scrap().get_bridge_state()
    if state:
        text = "Most jest otwarty przez "
    else:
        text = "Most jest zamkniety przez "

    time_left = Scrap().get_time_left()

    if time_left["hours"] == 0:
        text += "{}min".format(time_left["minutes"])
    else:
        text += "{}h i {}min.".format(time_left["hours"], time_left["minutes"])

    return web.Response(text=text)

if __name__ == "__main__":
    app = web.Application()
    app.add_routes([web.get('/', handle)])
    web.run_app(app)
