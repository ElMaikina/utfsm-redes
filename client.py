import socket

# Constantes de la conexion
HEADERSIZE = 10
IP = "localhost"
PORT = 8000

# Crea un socket para conectarse al servidor intermediario
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

game_is_running = True

def run():
    new_msg_in = True
    full_msg_in = ""
    msg_in_len = 0

    while True:
        msg_in = s.recv(16)

        if msg_in[:HEADERSIZE] == b'':
            print("No hay respuesta...")
            return

        if new_msg_in:
            msg_in_len = int(msg_in[:HEADERSIZE])
            new_msg_in = False
    
        full_msg_in += msg_in.decode("utf-8")
    
        if len(full_msg_in)-HEADERSIZE == msg_in_len:
            print(full_msg_in[HEADERSIZE:])
            new_msg_in = True
            full_msg_in = ""
            return

if __name__ == '__main__':
    while game_is_running:
        run()
        play = input("->")

