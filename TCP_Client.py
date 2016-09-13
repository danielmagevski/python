import socket

def Main():
    host = '127.0.0.1'
    port = 5000
    m = 'Recebendo conexao de: '

    s = socket.socket()
    s.connect((host, port))

    message = raw_input("-> ")
    while message != 'q':
        s.send(message)
        data = s.recv(1024)
        print (m) + str(data)
        message = raw_input("-> ")
    s.close()

if __name__ == '__main__':
    Main()
