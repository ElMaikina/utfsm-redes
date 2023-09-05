import socket

# Constantes de la conexion
HEADERSIZE = 10
IP = "localhost"
PORT = 8000

# Crea un socket para establecer el servidor intermediario
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Se conecta y recibe informacion
server_socket.bind((IP, PORT))
server_socket.listen(1)

socket_list = [server_socket]

clients = {}

while True:
    client_socket, address = server_socket.accept()
    #print(f"Stablished new conection from adress: {address}")
    msg = "Welcome to the server"
    msg = f"{len(msg):<{HEADERSIZE}}" + msg
    client_socket.send(bytes(msg, "utf-8"))

