import socket


PORT = 9009
HOST = ''


def chat_server():
    server_socket = socket.socket()
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print("Server started")
    client_socket, client_address = server_socket.accept()
    print("Client {} connected".format(address))
    send_message(client_socket, "Welcome!")
    client_socket.close()
    server_socket.close()