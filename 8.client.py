import socket
import sys
import json
class Employee:
    def __init__(self, name, age,company):
        self.name = name
        self.age = age
        self.company= company
class Customer:
    def __init__(self, name, age, company):
        self.name = name
        self.age = age
        self.company = company
if __name__ == "__main__":
    e1=Employee("Maha","21","LTTS")
    c1=Customer("Harish","22","Byjus")
    jsonstr1=json.dumps(e1.__dict__).encode('utf-8')
    jsonstr2=json.dumps(c1.__dict__).encode('utf-8')
try:
    s=socket.socket()
except socket.error as err:
    print("Socket Error because of %s" % (err))
port=1500
ipaddress="127.0.0.1"
try:
    s.connect((ipaddress,port))
    s.send(jsonstr1)
    s.send(jsonstr2)
except socket.gaierror:
    print("There was an error resolving host")
    sys.exit()
