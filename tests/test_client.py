# -*- coding: utf-8 -*-
import mock
import json

from keyard_client import KeyardClient


class TestKeyardClient(object):

    def setup_method(self, method):
        self.client = KeyardClient('localhost:8001')

    @mock.patch('keyard_client.client.requests.post')
    def test_register(self, mock_post):
        mock_post.return_value = type('Request', (),
                                      {'text': '', 'status_code': 200})
        self.client.register('app', '0.1', 'localhost:8002')
        assert mock_post.called_with(
            'localhost:8001', headers={'content-type': 'application/json'},
            data={'name': 'app', 'version': '0.1', 'location':
                  'localhost:8002'})

    @mock.patch('keyard_client.client.requests.put')
    def test_health_check(self, mock_put):
        mock_put.return_value = type('Request', (),
                                     {'text': '', 'status_code': 200})
        self.client.health_check('app', '0.1', 'localhost:8002')
        assert mock_put.called_with(
            'localhost:8001', headers={'content-type': 'application/json'},
            data={'name': 'app', 'version': '0.1', 'location':
                  'localhost:8002'})

    @mock.patch('keyard_client.client.requests.delete')
    def test_unregister(self, mock_delete):
        mock_delete.return_value = type('Request', (),
                                        {'text': '', 'status_code': 200})
        self.client.unregister('app', '0.1', 'localhost:8002')
        assert mock_delete.called_with(
            'localhost:8001', headers={'content-type': 'application/json'},
            data={'name': 'app', 'version': '0.1', 'location':
                  'localhost:8002'})

    @mock.patch('keyard_client.client.requests.get')
    def test_get_service(self, mock_delete):
        result = {"result": 'locahost:8080'}
        mock_delete.return_value = type('Request', (),
                                        {'text': json.dumps(result),
                                         'status_code': 200})
        value = self.client.get_service('app')
        assert mock_delete.called_with(
            'localhost:8001', headers={'content-type': 'application/json'},
            data={'name': 'app', 'version': '0.1', 'location':
                  'localhost:8002'})
