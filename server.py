import socket
import sock_utils

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_ip = "127.0.0.1"
server_port = 8080
server_address = (server_ip, server_port)

server.bind(server_address)

server.listen(5)

while True:
    print("Ожидание подключения...")

    connection, client_address = server.accept()

    print(f"Подключено к: {client_address}")

    try:
        while True:
            incoming_message = sock_utils.receive(connection).decode(
                encoding="utf-8", errors="ignore"
            )

            if incoming_message == "/quit":
                break

            print(f"Сообщение от {client_address}: {incoming_message}")

            outgoing_message = input(f"Введите сообщение для {client_address}: ")

            connection.sendall(
                outgoing_message.encode(encoding="utf-8", errors="ignore")
            )

            if outgoing_message == "/quit":
                break

    finally:
        print(f"Соединение с {client_address} закрыто")

        connection.close()
