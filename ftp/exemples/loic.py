import socket
import sys
import time
import os
import struct

print("START SERVER")

SERVER_IP = ""
SERVER_PORT = 2121
BUFFER_SIZE = 1024

_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
_socket.bind((SERVER_IP, SERVER_PORT))
_socket.listen(1)
conn, addr = _socket.accept()
conn.send('220 connection started.\r\n'.encode())

print(f"CONNECTED TO {addr}")


def user_serv(_username):
    response_code = '430'
    if _username.upper() == "TEST":
        response_code = '331'
    conn.send(response_code.encode())


def quit_serv():
    conn.send('1'.encode())
    conn.close()
    _socket.close()
    os.execl(sys.executable, sys.executable, *sys.argv)


while True:
    data = conn.recv(BUFFER_SIZE)
    if not data:
        break
    try:
        data = data.decode()
        print(f'DATA RECEIVED -> {data}')

        data_arr = data.split('\r\n')[:-1]

        data = data_arr[0]
        print(data_arr)

        if data == "USER":
            user_serv(data_arr[1])
        elif data == "QUIT":
            quit_serv()
        else:
            conn.send('220 connection started.\r\n'.encode())

        data = None

    except UnicodeDecodeError:
        print("TLS -> CANNOT DECODE")
        pass

# code réponse --> https://fr.wikipedia.org/wiki/Liste_des_codes_des_réponses_d%27un_serveur_FTP
# commande --> https://fr.wikipedia.org/wiki/Liste_des_commandes_ftp
