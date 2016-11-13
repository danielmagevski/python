#!/usr/bin/python3
from socket import *

HOST = ''
PORT = int(input("What's port server is running: "))

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))

while True:
         msg = input("Client: ")
        s.send(msg.encode())

        data = s.recv(1024)
        print("Server: ", data.decode())
s.close


