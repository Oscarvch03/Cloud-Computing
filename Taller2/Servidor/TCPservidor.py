########################################################################
# IMPORTAR LIBRERIAS ###################################################

from socket import *


########################################################################
# DEFINICION DE METODOS ################################################

def saldo():
    # Retorna el saldo actual guardado en saldo.txt
    file = open("saldo.txt", 'r')
    sld = file.readlines()[-1]
    file.close()
    return sld

def debitar(X):
    # Disminuye el saldo guardado en saldo.txt
    file = open("saldo.txt", 'a')
    sld = float(saldo())
    ans = ""
    if(X <= sld):
        file.write("\n" + str(sld - X))
        ans += "OK"
    else:
        ans += "Saldo Insuficiente"
    file.close()
    return ans

def acreditar(Y):
    # Aumenta el saldo guardado en saldo.txt
    file = open("saldo.txt", 'a')
    sld = float(saldo())
    ans = str(sld + Y) 
    file.write("\n" + ans)
    file.close()
    ans = "Nuevo Saldo => " + ans
    return ans


########################################################################
# BLOQUE PRINCIPAL DE INSTRUCCIONES ####################################

servidorPuerto = 12000
servidorSocket = socket(AF_INET, SOCK_STREAM)
servidorSocket.bind(('', servidorPuerto))
servidorSocket.listen(1)
print("\nEl servidor está listo para recibir Consultas. \n")

while(1):
    conexionSocket, clienteDireccion = servidorSocket.accept()
    # print("Conexión establecida con ", clienteDireccion)
    mensaje = str(conexionSocket.recv(1024), "utf-8")
    print("Mensaje recibido de " + clienteDireccion[0] +  ": " + mensaje)
    msg = mensaje.split()
    # print(msg)

    mensajeRespuesta = ""
    
    if(msg[0] == "saldo"):
        mensajeRespuesta += saldo()
    elif(msg[0] == "debitar"):
        X = float(msg[1])
        mensajeRespuesta += debitar(X)
    elif(msg[0] == "acreditar"):
        Y = float(msg[1])
        mensajeRespuesta += acreditar(Y)
    elif(msg[0] == "q"):
        break
    else:
        mensajeRespuesta += "No se pudo realizar la Consulta. "

    # print(mensaje)
    # mensajeRespuesta = mensaje.upper()

    print("Mensaje respuesta:", mensajeRespuesta, "\n")
    conexionSocket.send(bytes(mensajeRespuesta, "utf-8"))
    conexionSocket.close()