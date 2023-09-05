import socket

# Constantes de la conexion
HEADERSIZE = 10
IP = "localhost"
PORT = 8000

# Crea un socket para conectarse al servidor intermediario
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

# Recibe un mensaje en formato UTF-8
new_msg_in = True
full_msg_in = ""

while True:
    msg_in = s.recv(16)
    if new_msg_in:
        #print(f"New message length: {msg_in[:HEADERSIZE]}")
        msg_in_len = int(msg_in[:HEADERSIZE])
        new_msg_in = False

    full_msg_in += msg_in.decode("utf-8")

    if len(full_msg_in)-HEADERSIZE == msg_in_len:
        #print("Full message recieved")
        print(full_msg_in[HEADERSIZE:])
        new_msg_in = True
        full_msg_in = ""

print(full_msg)

