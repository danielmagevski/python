#!/usr/bin/python3
from socket import *

HOST = ''
PORT = int(input("What's port server going to run: "))
s= socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

while True:
    print("Waiting connetion on ", (PORT))
    c, addr = s.accept()
    print("Client connected ", addr)

    while True:
        data = c.recv(1024)
        print("", data.decode())

        res = input("Server: ")

        c.send(res.encode())

    c.close()
