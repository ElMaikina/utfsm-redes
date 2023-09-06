import socket

# Constantes de la conexion
HEADERSIZE = 10
IP = "localhost"
PORT = 8000

# Crea un socket para conectarse al servidor intermediario
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect((IP, PORT))

# Variable que mantiene el juego funcionando
game_is_running = True

# Recibe el mensaje del servidor
def listen_to_server():
    new_message_in = True # Llego carta?
    full_message_in = ""  # Mensaje completo
    message_in_len = 0    # Largo del mensaje

    while True:
        message_in = server_socket.recv(16)
        #print(f"Nuevo mensaje sin decodificar: {message_in}")

        # Si el mensaje es vacio, avisar al usuario y salir
        if message_in[:HEADERSIZE] == b'':
            print("No hay respuesta...")
            return

        # Si llego un mensaje, buscar el largo
        if new_message_in:
            message_in_len = int(message_in[:HEADERSIZE])
            new_message_in = False
   
        # Decodificar el mensaje en formato UTF-8
        full_message_in += message_in.decode("utf-8")
   
        # Si el mensaje leido es igual a la ultima porcion
        # del mensaje total, mostrarlo por pantalla y salir
        # de la funcion
        if len(full_message_in)-HEADERSIZE == message_in_len:
            print(full_message_in[HEADERSIZE:])
            new_message_in = True
            full_message_in = ""
            return

# Analiza la respuesta del jugador humano
def analyze_play(play):
    if play == "Salir":
        print("Saliendo del juego")
        game_is_ruinning = False
        exit()

# Funcion main
if __name__ == '__main__':
    while game_is_running:
        listen_to_server()
        play = input("->")
        analyze_play(play)

