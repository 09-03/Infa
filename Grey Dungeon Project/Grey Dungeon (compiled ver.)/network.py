import socket


class Network():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = server
        self.port = port
        self.address = (self.server, self.port)
        self.status = self.connect()


    def getstatus(self):
        return self.status


    def connect(self):
        try:
            self.client.connect(self.address)
            return self.client.recv(2048).decode()

        except:
            pass


    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
            
        except socket.error as e:
            print(e)


file = open("ipconfig.txt", "r")
ipconfig = file.readlines()
server = ipconfig[0].replace("\n", "")
port = int(ipconfig[1])
file.close()
