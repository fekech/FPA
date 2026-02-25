import  os , socket, threading

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('26.69.212.179', 5000)
socket.bind(address)
socket.listen(5)

print(f"Сервер запущен на {address[0]}:{address[1]}")


while True:
    try:
        # Принимаем входящее соединение
        client_socket, client_address = socket.accept()
        print(f"Подключен клиент: {client_address[0]}:{client_address[1]}")
        print(client_socket.recv(1024).decode('utf-8'))
    finally:
        # Закрываем соединение с клиентом
        client_socket.close()
