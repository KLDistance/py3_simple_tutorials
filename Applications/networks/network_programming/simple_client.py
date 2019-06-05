from socket import *

def send(message) : 
    # here use TCP SOCK_STREAM, for UDP is SOCK_DGRAM
    sock = socket(AF_INET, SOCK_STREAM)
    # define destination and port
    sock.connect(('127.0.0.1', 9999))
    # encode the string into networking formats
    sock.send(message.encode())
    # wait until the server responds
    receive_message = sock.recv(1024).decode()
    sock.close()
    return receive_message

if __name__ == '__main__' : 
    recv_str = send("Hey guy! I am client!")
    print(recv_str)


# actually each time we want to send a message, we have to rebuild the TCP connection over and over again
# this is how HTTP 1.0 does
# HTTP 1.1/2.0 use "keep alive" to avoid frequent reconstruction of TCP connection to avoid redundant usage of bandwidth