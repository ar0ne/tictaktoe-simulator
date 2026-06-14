"""
Minimal web service that returns random 'turn' for TicTacToe simulation.
To install required dependencies run:

>>> uv sync --group demo

To run demo simulation:

>>> uv run server.py
======== Running on http://0.0.0.0:8080 ========
"""
import random

from aiohttp import web


def next_turn() -> str:
    return str(random.choice(range(9)))


async def index(request):
    return web.Response(text=next_turn())


app = web.Application()
app.router.add_get("/", index)
web.run_app(app)
