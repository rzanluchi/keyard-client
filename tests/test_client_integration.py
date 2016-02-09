# -*- coding: utf-8 -*-
import json
import pytest

from keyard_client import KeyardClient, testutils


@pytest.mark.skipif(not testutils.keyard_is_available(), reason="keyard is missing")
class TestKeyardClient(object):

    def setup_method(self, method):
        self.client = KeyardClient('http://127.0.0.1:8000')

    def test_register(self):
        response = self.client.register('app', '0.1', 'localhost:8002')
        assert response is True

    def test_health_check(self):
        response = self.client.health_check('app', '0.1', 'localhost:8002')
        assert response is True

    def test_unregister(self):
        response = self.client.unregister('app', '0.1', 'localhost:8002')
        assert response is True

    def test_get_service(self):
        result = {"result": ['localhost:8080']}
        value = self.client.get_service('app')
        assert result == value
