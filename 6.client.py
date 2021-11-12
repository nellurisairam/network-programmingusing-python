import socket
import sys
import json
jsonResult={"first":"Hi","second":"Maha"}
jsonResult=json.dumps(jsonResult).encode('utf-8')
try:
    s=socket.socket()
except socket.error as err:
    print("Socket Error because of %s" %(err))
port=1500
ipaddress="127.0.0.1"
try:
    s.connect((ipaddress,port))
    s.send(jsonResult)
except socket.gaierror:
    print("There was an error resolving host")
    sys.exit()