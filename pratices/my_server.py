from socket import *

tcp_server_socket = socket(AF_INET, SOCK_STREAM)

address = ('127.0.0.1', 8081)

tcp_server_socket.bind(address)

tcp_server_socket.listen(5)

while True:
    new_socket, client_addr = tcp_server_socket.accept()
    while True:
        recv_data = new_socket.recv(1024)
        if len(recv_data) > 0:
            print('recv:', recv_data)
        else:
            continue
        sendData = "OK"
        new_socket.send(bytes(sendData.encode("utf8")))

    new_socket.close()

tcp_server_socket.close()
