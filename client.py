import socket

# Crea un socket para conectarse al servidor intermediario
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Direccion del intermediario
add = ('localhost', 8000)

# Se conecta y recibe informacion
s.connect(add)

# Recibe un mensaje en formato UTF-8
msg = s.recv(1024)
print(msg.decode("utf-8"))

