import socket

HOST = ''              # Ip Server.
PORT = 8000            # Port Server.
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

while True:
    print("Initializing server on port: \n") + str(PORT)
    print("Waiting Clients.... \n")
    con, client = tcp.accept()
    print 'Conect by', client
    while True:
        msg = con.recv(1024)
        if not msg: break
        print cliente, msg
    print ("Finishing client connection \n"), client
    con.close()
