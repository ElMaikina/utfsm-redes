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

# Funcion main
if __name__ == '__main__':
    while game_is_running:
        print("- Seleccione una opcion\n1- Jugar\n2- Salir")
        play = input("->")
        if(play=="2"):
            game_is_running=False
            msg = "Finalizar"
            server_socket.send(msg.encode())
        elif(play=="1"):
            print("--------Conecta4--------")
            flag=True
            Tablero=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
            PrintTablero(Tablero)
            while(flag):
                jugada = input('Ingrese la columna en la que desea jugar su ficha: ')
                server_socket.send(jugada.encode())
                Tablero=CambiarTablero(Tablero,int(jugada),1)
                PrintTablero(Tablero)
                response = server_socket.recv(1024).decode()
                #Condiciones de Vicotria
                if(response=="Ganaste"):
                    flag2=False
                    print(">>>Gano el Jugador<<<")
                    print("==============================")
                elif(response=="Gano CPU"):
                    flag2=False
                    print(">>>Gano la CPU<<<")
                    print("==============================")
                else:#condicion de siguiente Turno
                    tablero=CambiarTablero(Tablero,int(response),2)
                    PrintTablero(Tablero)
                
                


