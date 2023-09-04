import socket

# Constantes de la conexion
HEADERSIZE = 10
IP = "localhost"
PORT = 8000

# Crea un socket para conectarse al servidor intermediario
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

# Recibe un mensaje en formato UTF-8
new_msg = True
full_msg = ""
while True:
    msg = s.recv(16)
    if new_msg:
        #print(f"New message length: {msg[:HEADERSIZE]}")
        msg_len = int(msg[:HEADERSIZE])
        new_msg = False

    full_msg += msg.decode("utf-8")

    if len(full_msg)-HEADERSIZE == msg_len:
        #print("Full message recieved")
        print(full_msg[HEADERSIZE:])
        new_msg = True
        full_msg = ""

print(full_msg)

