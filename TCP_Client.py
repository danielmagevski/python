import socket

HOST = '127.0.0.1'     # Ip Server
PORT = 8000            # Port Server

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

print("Digite a mensagem")
print 'Use CTRL+X to exit\n'
msg = raw_input()
while msg <> '\x18':
    tcp.send (msg)
    msg = raw_input()
tcp.close()
