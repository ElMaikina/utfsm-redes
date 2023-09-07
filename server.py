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
server_socket.listen(5)
client_socket, address = server_socket.accept()

# Variable que mantiene el juego funcionando
game_is_running = True
def CambiarTablero(Tablero, col, player):
    # Find the first available row in the specified column
    for row in range(len(Tablero) - 1, -1, -1):
        if Tablero[row][col] == 0:
            Tablero[row][col] = player
            return Tablero
    return None
def PrintTablero(tablero):
    PrintTable=[["","","","","",""],["","","","","",""],["","","","","",""],["","","","","",""],["","","","","",""],["","","","","",""],["","","","","",""]]
    print(".  0 | 1 | 2 | 3 | 4 | 5")
    for x in range(6):
        for y in range(6):
            if tablero[x][y]==0:
                PrintTable[x][y]="\u26AB"
            elif tablero[x][y]==1:
                PrintTable[x][y]="\U0001F7E2"
            else:
                PrintTable[x][y]="\U0001F7E0"
    for x in range(6):
        string="{} {}  {}  {}  {}  {}  {}"
        print(string.format(x,PrintTable[x][0],PrintTable[x][1],PrintTable[x][2],PrintTable[x][3],PrintTable[x][4],PrintTable[x][5]))
def ComprobarEstado(tablero):
    def check_line(row, col, dr, dc, player):
        for _ in range(4):
            if row < 0 or row >= len(tablero) or col < 0 or col >= len(tablero[0]) or tablero[row][col] != player:
                return 0
            row += dr
            col += dc
        return player

    for player in [1, 2]:
        for row in range(len(tablero)):
            for col in range(len(tablero[0])):
                for dr, dc in [(0, 1), (1, 0), (1, 1), (-1, 1)]:
                    winner = check_line(row, col, dr, dc, player)
                    if winner != 0:
                        return winner
    
    return 0
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
#
if __name__ == '__main__':
    try:
        serverPort = 8001
        IP = 'localhost'
        conecta4_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except:
        print("Error: No se pudo conectar con servidor conecta4")
        game_is_running=False
    if(game_is_running):
        print("Conexiones Verificadas, Iniciando Conecta4")
        Tablero=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        PrintTablero(Tablero)
    while(game_is_running):
        PlayerMessage = client_socket.recv(1024).decode()
        if(PlayerMessage=="Salir"):
            print("Saliendo del juego")
            msg="Salir"
            conecta4_socket.send(msg.encode())
            game_is_ruinning = False
            exit()
        else:
            print("Jugada Player-> Columna ({})".format(PlayerMessage))
            Tablero=CambiarTablero(Tablero,int(PlayerMessage[0]),1)
            PrintTablero(Tablero)
            if(ComprobarEstado(Tablero)==1):
                Tablero=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]#Reseteo del tablero por si se quiere un siguiente Juego
                msg="Ganaste"
                client_socket.send(msg.encode())#Enviar al Cliente la victoria del Jugador
                conecta4_socket.sendto("Reiniciar".encode(), (IP, serverPort))#Enviar al server el reseteo del juego para prepararse
                print(">>>Gano el Jugador<<<")
                print("==============================")
            else:
                msg=PlayerMessage[0]
                conecta4_socket.sendto(str(msg).encode(), (IP, serverPort))
                try:
                    serverPort2, _ = conecta4_socket.recvfrom(1024)#Recibir puerto desde el server por UDP1
                    serverPort2=int(serverPort2.decode())
                    print("Recibido Puerto SOCKET UDP2 :{}".format(serverPort2))
                    serverSocket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    serverSocket2.bind(("",serverPort2))
                    print("Conectado Puerto SOCKET UDP2 :{}".format(serverPort2))
                except:
                    pass
                serverSocket2.sendto(str(PlayerMessage).encode(), (IP, serverPort2))
                Mensaje, addr2 = serverSocket2.recvfrom(1025)#Jugada desde el Server UDP2
                serverSocket2.close()
                JugadaCPU=Mensaje.decode()
                print(JugadaCPU)
                print("recibida Jugada desde SOCKET UDP2 {}".format(JugadaCPU))
                print("Jugada CPU-> Columna ({})".format(JugadaCPU))
                print("==============================")
                Tablero=CambiarTablero(Tablero,int(JugadaCPU),2)
                PrintTablero(Tablero)
                if(ComprobarEstado(Tablero) == 2):#Condicion Victoria del Server
                    Tablero=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
                    msg="Gano CPU"
                    client_socket.send(msg.encode())#Avisar al cliente de que gano el servidor
                    conecta4_socket.sendto("Reset".encode(), (IP, serverPort))#Avisar al conecta4 de que se tiene que reiniciar
                    print(">>>Gano la CPU<<<")
                    print("==============================")

                else:#Jugada normal donde nadie gano y se envia el jugada de cpu al cliente
                    client_socket.send(JugadaCPU.encode())


