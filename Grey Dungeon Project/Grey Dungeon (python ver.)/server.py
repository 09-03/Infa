import socket
from _thread import *


def Read_status(str):
    str = str.split(",")
    return int(str[0]), int(str[1]), int(str[2]), int(str[3]), int(str[4]), int(str[5]), int(str[6])


def Make_status(tup):
    return str(tup[0]) + "," + str(tup[1]) + "," + str(tup[2]) + "," + str(tup[3]) + "," + str(tup[4]) + "," + str(tup[5]) + "," + str(tup[6])


def threaded_client(connection, player):
    connection.send(str.encode(Make_status(status[player])))
    reply = ""
    while True:
        try:
            data = Read_status(connection.recv(2048).decode())
            status[player] = data
            if not data:
                print("Disconnected")
                break

            else:
                if player == 1:
                    reply = status[0]

                else:
                    reply = status[1]

                print("Получено: ", data)
                print("Отправляю: ", reply)

            connection.sendall(str.encode(Make_status(reply)))

        except:
            break

    print("Потеря Соединения")
    connection.close()


file = open("ipconfig.txt", "r")
ipconfig = file.readlines()
server = ipconfig[0].replace("\n", "")
port = int(ipconfig[1])
file.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.bind((server, port))

except socket.error as e:
    print(e)

sock.listen(2)
print("Ожидание Подключения, Сервер Готов к Работе")
status = [(250, 250, 100, 100, 0, 1200, 800), (2150, 1350, 100, 100, 0, 1200, 800)]
currentPlayer = 0
while True:
    connection, address = sock.accept()
    print("Подключен к: ", address)
    start_new_thread(threaded_client, (connection, currentPlayer))
    currentPlayer += 1
