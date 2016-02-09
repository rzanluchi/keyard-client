# -*- coding: utf-8 -*-
import falcon
from keyard_client import KeyardClient


class App2(object):

    def on_get(self, req, resp):
        resp.body = "World"


app = falcon.API()
app.add_route('/app2', App2())
client = KeyardClient('http://127.0.0.1:8000')
client.register('client2', '1.0', 'localhost:8002')
