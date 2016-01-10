import socket


def keyard_is_available():
    try:
        socket.create_connection(('127.0.0.1', 8001), 1.0)
    except socket.error:
        return False
    else:
        return True
