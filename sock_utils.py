def receive(socket, chunk_size=1024):
    data = b""

    while True:
        chunk = socket.recv(chunk_size)

        if not chunk:
            break

        data += chunk

        if len(chunk) < chunk_size:
            break

    return data
