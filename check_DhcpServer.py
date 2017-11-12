#!/usr/bin/python

from scapy.all import *
import os
 
if os.geteuid() != 0:
	exit("You need to root privileges")

print("\nPress Ctrl+D to stop\n")

conf.checkIPaddr = False
fam,hw = get_if_raw_hwaddr(conf.iface)
dhcp_discover = Ether(dst="ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0",dst="255.255.255.255")/UDP(sport=68,dport=67)/BOOTP(chaddr=hw)/DHCP(options=[("message-type","discover"),"end"])
ans, unans = srp(dhcp_discover, multi=True)
print("\n")
ans.summary()
