#!/bin/python3

_author_= "Daniel Magevski"
import smtplib

##Hotmail##
server = smtplib.SMTP('smtp.live.com', 587)
server.starttls()

server.login("Email", "password)

msg = "Send e-mail from Python"
server.sendmail("From", "To", msg)
print("Message was sent sucessefull")
server.quit()
