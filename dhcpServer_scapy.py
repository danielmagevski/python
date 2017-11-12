#!/usr/bin/python
from scapy.all import DHCP_am
from scapy.base_classes import Net
import os
 
if os.geteuid() != 0:
	exit("You need to root privileges")

print("\nPress Ctrl+C to stop\n")

dhcp_server = DHCP_am(iface='eth1', domain='danielbr.me',
                      pool=Net('172.16.0.0/24'),
                      gw='172.16.0.254',
                      renewal_time=600, lease_time=3600)
dhcp_server()
