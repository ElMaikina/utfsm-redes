package main

import (
    "fmt"
    "net"
    "math/rand"
	"time"
    "strconv"
)



func main() {
    IP := "localhost:"
    PORT :="8001"
    serverAddr := IP+PORT
    udpAddr, err := net.ResolveUDPAddr("udp", serverAddr)			//Chequea la validez de la direccion del servidor UDP a crear
    if err != nil {
        fmt.Println("Error al resolver la direccion del servidor:", err)
    }

    conn, err := net.ListenUDP("udp4", udpAddr)
    if err != nil { 
        fmt.Println(err)
    }
    fmt.Println("Conexion UDP creada en el puerto: ",PORT)
    defer conn.Close()
Reset:
    rand.Seed(time.Now().Unix())
    Tablero:=[36]int{0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0}
    fmt.Println(Tablero)
    buffer := make([]byte, 1024)
	buffer2 := make([]byte, 1025)
    print(buffer2)
    for true{
        //Conexion UDP2 para enviar jugada al servidor
		PORT2 := rand.Intn(65535-8000) + 8000 //Generar puerto aleatorio
		s2, err := net.ResolveUDPAddr("udp4", ":"+strconv.Itoa(PORT2))
		if err != nil { //Errores de conexion
			fmt.Println(err)
			return
		}

		connection2, err := net.ListenUDP("udp4", s2)
		if err != nil { //Errores de conexion
			fmt.Println(err)
			return
		} 

		fmt.Println("Puerto UDP2 Aleatorio :", PORT2)
		n, addr, _ := conn.ReadFromUDP(buffer) //Recepcion de orden de jugar
		msg := string(buffer[:n])
		_, _ = conn.WriteToUDP([]byte(strconv.Itoa(PORT2)), addr) // Enviar Puerto2
		fmt.Println("Recibi el msg del Server intermedio")
        if msg == "Finalizar" { 
			fmt.Println("Juego Finalizado")
			break
        }else if msg == "Reset" { //Resetear Juego comenzando desde label RESET
			fmt.Println("Se ha reseteado el Juego")
			connection2.Close()
			goto Reset
        }else { 
            Intmsg, _ := strconv.Atoi(msg) //Posicion de la jugada del cliente
            for x := 0; x < 6; x++ {
                if Tablero[x*6+Intmsg]!=0{
                    Tablero[x-1+Intmsg]=1;
                }else if x==5{
                    Tablero[x-1+Intmsg]=1;
                }
            }

        }
        START:
            random := rand.Intn(6)
            if Tablero[random] != 0 {
                goto START //En caso de que la columna esté llena generar otra aleatoria
            }
            fmt.Println("Envio movimiento aleatorio")
            for x := 0; x < 6; x++ {
                if Tablero[x*6+random]!=0{
                    Tablero[x-1+random]=2;
                }
            }
            _, addr2, _ := connection2.ReadFromUDP(buffer2) //Recibir address desde intermedio
            fmt.Println("Recibir msg UDP2")
            fmt.Println("Tablero:", Tablero)
            fmt.Println("columna:", msg)
            fmt.Println("direccion:", addr2)
            fmt.Println("==============================")
            response := []byte(strconv.Itoa(random))       
            _, _ = connection2.WriteToUDP(response, addr2) //Enviar jugada al server
            connection2.Close()
    }    
}
