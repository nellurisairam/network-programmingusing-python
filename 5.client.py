import socket, json

HOST = 'localhost'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
arr = ([1,2,3,4,5,6],[1,2,3,4,5,6])
data_string = json.dumps(arr).encode('utf-8')
s.send(data_string)

data = s.recv(4096)
data_arr = json.loads(data)
s.close()
print('Received', repr(data_arr))