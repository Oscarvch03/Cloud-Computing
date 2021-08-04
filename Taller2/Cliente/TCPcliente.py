########################################################################
# IMPORTAR LIBRERIAS ###################################################

from socket import *


########################################################################
# BLOQUE PRINCIPAL DE INSTRUCCIONES ####################################

servidorNombre = "127.0.0.1"  # DIRECCION IP DEL SERVIDOR
servidorPuerto = 12000  # PUERTO DE COMUNICACION
clienteSocket = socket(AF_INET, SOCK_STREAM)
clienteSocket.connect((servidorNombre, servidorPuerto))

print("\nBienvenido a su Zona Transaccional. Puede realizar las siguientes Consultas:")
print("    - saldo")
print("    - debitar X")
print("    - acreditar Y")

mensaje = input("\nConsulta: ")

clienteSocket.send(bytes(mensaje, "utf-8"))
mensajeRespuesta = clienteSocket.recv(1024)
print("Respuesta: " + str(mensajeRespuesta, "utf-8") + "\n")
    
clienteSocket.close()