import socket
port=60
host=socket.gethostname()
ip=socket.gethostbyname(host)
buffer_size=1024
msg=b'Hello Ammu'
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip,port))
s.send(msg)
data=s.recv(buffer_size)
s.close()