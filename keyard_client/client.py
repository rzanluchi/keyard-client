# -*- coding: utf-8 -*-
import json
import requests


class KeyardClient(object):

    def __init__(self, keyard_host):
        self.keyard_host = keyard_host + "/keyard"

    def _make_request(self, method, data):
        requests_method = getattr(requests, method.lower())
        kwargs = {
            'headers': {'content-type': 'application/json'}
        }
        if method == "GET":
            kwargs.update({'params': data})
        else:
            kwargs.update({'data': json.dumps(data)})
        return requests_method(self.keyard_host, **kwargs)

    def register(self, name, version, location):
        method = "POST"
        data = {'service_name': name, 'version': version, 'location': location}
        body = self._make_request(method, data)
        if body.status_code == 200:
            return True
        else:
            raise Exception(body.text)

    def unregister(self, name, version, location):
        method = "DELETE"
        data = {'service_name': name, 'version': version, 'location': location}
        body = self._make_request(method, data)
        if body.status_code == 200:
            return True
        else:
            raise Exception(body.text)

    def health_check(self, name, version, location):
        method = "PUT"
        data = {'service_name': name, 'version': version, 'location': location}
        body = self._make_request(method, data)
        if body.status_code == 200:
            return True
        else:
            raise Exception(body.text)

    def get_service(self, name, version=None):
        method = "GET"
        data = {'service_name': name}
        if version:
            data.update({'version': version})
        body = self._make_request(method, data)
        if body.status_code == 200:
            return json.loads(body.text)
        else:
            raise Exception(body.text)
