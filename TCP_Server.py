import socket

HOST = ''              # Endereco IP do Servidor
PORT = 8000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

while True:
    print("Iniciando servidor na porta: \n") + str(PORT)
    print("Aguardando Clientes.... \n")
    con, cliente = tcp.accept()
    print 'Concetado por', cliente
    while True:
        msg = con.recv(1024)
        if not msg: break
        print cliente, msg
    print ("Finalizando conexao do cliente\n"), cliente
    con.close()
