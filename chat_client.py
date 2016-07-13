import socket


def send_message():
    message = input('Type a message \n')
    s.send(message.encode())


def setup_connection():
    ip = '10.0.17.55'
    port = '9009'
    s = socket.socket()
    s.connect((ip, 9009))
    return s


if __name__ == '__main__':
    client_socket = setup_connection()
    while True:
        buffer = client_socket.recv(1024)
        if not buffer:
            break
        print(buffer.decode())

