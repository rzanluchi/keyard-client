# -*- coding: utf-8 -*-
import falcon
import requests
import json
from keyard_client import KeyardClient


class App1(object):

    def __init__(self, *args, **kwargs):
        super(App1, self).__init__(*args, **kwargs)
        self.client = KeyardClient('http://127.0.0.1:8000')

    def on_get(self, req, resp):
        app2_host = self.client.get_service('client2', )
        app2_value = requests.get("http://{0}/app2".format(app2_host['result'][0]))
        resp.body = "Hello {0}".format(app2_value.text)


app = falcon.API()
app.add_route('/client1', App1())
