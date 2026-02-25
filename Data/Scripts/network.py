import socket

socket.setdefaulttimeout(25)

def NT_KeepConnection(address = ('127.0.0.1',5000)):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(address)
        client_socket.close()
        return True
    except ConnectionRefusedError:
        return False
    except Exception as e:
        print(f"Произошла ошибка: {e}")