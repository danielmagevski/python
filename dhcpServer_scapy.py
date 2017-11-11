#This program need to the scapy installed 
from scapy.all import DHCP_am
from scapy.base_classes import Net

dhcp_server = DHCP_am(iface='eth1', domain='danielbr.me',
                      pool=Net('172.16.0.0/24'),
                      gw='172.16.0.254',
                      renewal_time=600, lease_time=3600)
dhcp_server()
