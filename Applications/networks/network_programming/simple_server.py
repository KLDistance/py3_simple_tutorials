from socket import *

def echo() : 
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('', 9999))
    sock.listen(1)
    print('The server is ready to receive.')
    while True :
        connSock, addr = sock.accept()
        recv_sentence = connSock.recv(1024).decode()
        connSock.send(('Here is the server! I have received your request. Your sent sentence is: ' + recv_sentence).encode())
        connSock.close()
    
if __name__ == '__main__' : 
    try : 
        echo()
    except KeyboardInterrupt : 
        pass
    finally :
        print()