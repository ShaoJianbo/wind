
from socket import *

tcp_client_socket = socket(AF_INET, SOCK_STREAM)

address = ("localhost", 8081)

tcp_client_socket.connect(address)

while True:
    send_data = "client->"
    if len(send_data)>0:
        tcp_client_socket.send(bytes(send_data.encode("utf8")))
    else:
        break

    recv_data = tcp_client_socket.recv(1024)
    print("recv_data->", recv_data)

    tcp_client_socket.close()