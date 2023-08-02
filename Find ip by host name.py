import socket
import time
while(True):

    print("[1]Find IP by Host-name")
    print("[2]Find Host-name by IP")
    print("[3]Exit")
    print(" ")
    ch = int(input("Choose an option: "))
    if(ch == 1):
        host_name = input("Enter the host name: ")
        ip = socket.gethostbyname(host_name)
        print("IP ADDRESS: " + ip)
        print(" ")
        time.sleep(3)

    if(ch == 2):
        IP = input("Enter the IP Address: ")
        host = socket.gethostbyaddr(IP)
        print("Host-Name: " + str(host))
        print(" ")
        time.sleep(3)
        
    if(ch == 3):
        exit(0)
