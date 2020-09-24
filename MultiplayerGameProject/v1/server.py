import socket
from _thread import *
import sys

server = "192.168.0.100"
port = 5555

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.bind((server, port))
except socket.error as e:
    print(e)

sock.listen(2)
print("Ожидание Подключения, Сервер Готов к Работе")

def Read_Pos(str):
    str = str.split(",")
    return int(str[0]) ,int(str[1])


def Make_Pos(tup):
    return str(tup[0]) + "," + str(tup[1])

pos =[(0, 0), (100, 100)]

def threaded_client(connection, player):
    connection.send(str.encode(Make_Pos(pos[player])))
    reply = ""
    while True:
        try:
            data = Read_Pos(connection.recv(2048).decode())
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]
                print("Получено: ", data)
                print("Отправляю: ", reply)

            connection.sendall(str.encode(Make_Pos(reply)))
        except:
            break

    print("Потеря Соединения")
    connection.close()

currentPlayer = 0
while True:
    connection, address = sock.accept()
    print("Подключен к: ", address)

    start_new_thread(threaded_client, (connection, currentPlayer))
    currentPlayer += 1
