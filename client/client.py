

class KeyardClient(object):

    def __init__(self, keyard_host):
        self.keyard_host = keyard_host

    def _make_request(self, method, data):
        pass

    def register(self, name, version, location):
        method = "POST"
        data = {'name': name, 'version': version, 'location': location}
        self._make_request(method, data)

    def unregister(self, name, version, location):
        method = "DELETE"
        data = {'name': name, 'version': version, 'location': location}
        self._make_request(method, data)

    def health_check(self, name, version, location):
        method = "PUT"
        data = {'name': name, 'version': version, 'location': location}
        self._make_request(method, data)

    def get_serivce(self, name, version):
        method = "GET"
        data = {'name': name, 'version': version}
        self._make_request(method, data)
