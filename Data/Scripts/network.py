import socket

socket.setdefaulttimeout(25)

def ConnectionCheck(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ConnectionRefusedError:
            print(f'Не удалось подключиться к серверу {args[0][0]}:{args[0][1]}')
        except OSError:
            pass
        except Exception as e:
            print(f"Произошла неизвестная ошибка: {e}")
    return wrapper

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

@ConnectionCheck
def NT_SendData(address = ('127.0.0.1',5000),message="None"):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(address)
    client_socket.sendall(message.encode('utf-8'))
    client_socket.close()

@ConnectionCheck
def NT_ReadData(address = ('127.0.0.1',5000)):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(address)
    data = client_socket.recv(1024)
    client_socket.close()
    return data.decode('utf-8')
