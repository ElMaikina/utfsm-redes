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
client_socket, address = server_socket.accept()

game_is_running = True

def run():
    msg_out = ""
    msg_out += "\nBienvenido al Juego\n"
    msg_out += "Seleccione una opcion\n"
    msg_out += "1-Jugar\n"
    msg_out += "2-Salir"
    msg_out = f"{len(msg_out):<{HEADERSIZE}}" + msg_out
    client_socket.send(bytes(msg_out, "utf-8"))
    print("Message sent!")

if __name__ == '__main__':
    run()

