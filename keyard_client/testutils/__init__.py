import socket


def keyard_is_available(port=8000):
    try:
        socket.create_connection(('127.0.0.1', port), 1.0)
    except socket.error:
        return False
    else:
        return True
