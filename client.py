import socket
import sock_utils

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_ip = "127.0.0.1"
server_port = 8080
server_address = (server_ip, server_port)

client.connect(server_address)

try:
    while True:
        outgoing_message = input(f"Введите сообщение для {server_address}: ")

        client.sendall(outgoing_message.encode(encoding="utf-8", errors="ignore"))

        if outgoing_message == "/quit":
            break

        incoming_message = sock_utils.receive(client).decode(
            encoding="utf-8", errors="ignore"
        )

        if incoming_message == "/quit":
            break

        print(f"Сообщение от {server_address}: {incoming_message}")

finally:
    print(f"Соединение с {server_address} закрыто")

    client.close()
