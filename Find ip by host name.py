import socket

host_name = input("Enter the host name: ")
ip = socket.gethostbyname(host_name)
print("IP ADDRESS: " + ip)