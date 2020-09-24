import socket
from _thread import *
from player import Player
import pickle


server = "192.168.0.100"
port = 5555

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.bind((server, port))
except socket.error as e:
    print(e)

sock.listen(2)
print("Ожидание Подключения, Сервер Готов к Работе")

players = [Player(0, 0, 50, 50, (255, 0, 0)), Player(100, 100, 50, 50, (0, 0, 255))]

def threaded_client(connection, player):
    connection.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(connection.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                print("Получено: ", data)
                print("Отправляю: ", reply)

            connection.sendall(pickle.dumps(reply))
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
