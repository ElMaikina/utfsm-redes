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
server_socket.listen(2)
client_socket, address = server_socket.accept()

# Variable que mantiene el juego funcionando
game_is_running = True

# Enviarle el mensaje de bienvenida al jugador
def greet_the_client():
    message = ""
    message += "\nBienvenido al Juego\n"
    message += "Seleccione una opcion\n"
    message += "1-Jugar\n"
    message += "2-Salir"
    message = f"{len(message):<{HEADERSIZE}}" + message
    client_socket.send(bytes(message, "utf-8"))
    print("Server: message sent")
    return

# Enviarle un mensaje al cliente jugador
def talk_to_client():
    message = "Elija donde poner la pieza"
    message = f"{len(message):<{HEADERSIZE}}" + message
    client_socket.send(bytes(message, "utf-8"))
    print("Server: message sent")
    return

if __name__ == '__main__':
    greet_the_client()
    # Convertirlo en un loop y recibir mensajes del cliente
    #while game_is_running:
    talk_to_client()

