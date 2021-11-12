import socket
port=60
host=socket.gethostname()
ip=socket.gethostbyname(host)
buffer_size=30
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip,port))
s.listen(1)
c, addr =s.accept()
print('Connection Address', addr)
print("host=",host)
print("IP Address =", ip)
while True:
    data=c.recv(buffer_size)
    if not data:
        break
    print("Received data", data)
    #c.send(data)
    c.close()