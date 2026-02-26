import  os , socket, json, platform, threading

from cmd import CMD_AuthorLogo , CMD_Clear

CMD_AuthorLogo()

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = ('26.69.212.179', 5000)
try:
    socket.bind(address)
    print(f"Сервер запущен на {address[0]}:{address[1]}")
except Exception as e:
    print(f"Неизвестная ошибка {e}")
finally:
    socket.listen(5)

def main_body():
    FPAName = "SRV "+platform.node()+chr(92)+"$ "
    while True:
        UserCommand = input(FPAName)

def backend_loop():
    while True:
        try:
            # Принимаем входящее соединение
            client_socket, client_address = socket.accept()
            print('')
            print(f"Подключен клиент: {client_address[0]}:{client_address[1]}")
            print(client_socket.recv(1024).decode('utf-8'))
        finally:
            # Закрываем соединение с клиентом
            client_socket.close()

main_theard = threading.Thread(target=main_body)
backend_theard = threading.Thread(target=backend_loop)

main_theard.start()
backend_theard.start()