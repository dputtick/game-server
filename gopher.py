import socket
import sys

# initial configuration
port = 70   # default Gopher port
host = sys.argv[1]  # first argument is hostname
filename = sys.argv[2].encode()     # second argument is desired file path

def option1():
    '''Make and open socket using normal methods'''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # AF == "address family", INET == internet, SOCK_STREAM == socket type (TCP)
    # socket type could also be SOCK_DGRAM for UDP

    s.connect((host, port))
    # Opens a connection with "host" on "port"

    s.sendall(filename + b"\n")
    # Sends the entirety of the bytes in parens

    while True:
        buffer = s.recv(2048)
        if not buffer: # end while loop if buffer is empty, which would mean that
            break               # all data has been received
        print(buffer.decode())

def option2():
    '''do the same as above but with a file object'''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    fd = s.makefile(mode='rw')
    filename_notbytes = filename.decode()
    fd.write(filename_notbytes + "\n")
    for line in fd.readlines():
        print(line.decode())


def main():
    option1()

if __name__ == '__main__':
    main()
