import socket


PORT = 9009
HOST = '127.0.0.1'


def chat_server():
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print("Server started")
    client_socket, client_address = server_socket.accept()
    print("Client {} connected".format(client_address))
    send_message(client_socket, "Welcome!")
    client_socket.close()
    server_socket.close()


def send_message(socket, message):
    socket.sendall(message.encode())


if __name__ == '__main__':
    chat_server()
