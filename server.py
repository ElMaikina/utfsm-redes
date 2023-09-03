import socket

# Crea un socket para conectarse al servidor intermediario
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Direccion del intermediario
add = ('localhost', 8000)

# Se conecta y recibe informacion
s.bind(add)
s.listen(5)

# Ciclo de connexion con el intermediario
while True:
    sc, addr = s.accept()
    print(f"Se establecio una conexion desde {addr}")
    sc.send(bytes("Bienvenido al servidor!", "utf-8"))



