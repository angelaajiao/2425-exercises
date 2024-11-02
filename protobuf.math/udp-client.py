#!/usr/bin/env python3
#puerto 1234 ip: 192.168.8.224
import sys
import socket
import math_pb2

#controlamos que se escriba bien por teclado
if len(sys.argv) < 2:
    print(f'Usage: {sys.argv[0]} <host> <SUM o MUL> <numbers>')
    exit()

operation = int (sys.argv[2])
ip = sys.argv[1]

#creamos el array de numeros que son todos los de despues del argumento 3
numbers = [int(x) for x in sys.argv[3:]]

#Creamos el socket udp
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
destination = (sys.argv[1], 1234)

#Construimos la instancia de lo que queremos enviar
reading = math_pb2.Request()
reading.operation = operation
reading.numbers.extend(numbers)

#serializamos y mandamos la secuencia
data = reading.SerializeToString()
print(data)

sock.sendto(data, destination)
sock.close()

#recibimos el mensaje
sol, server = sock.recvfrom(1024)
#Creamos la instancia
response = math_pb2.Response()
#Deserializamos el mensaje
response.ParseFromString(sol)
print(f"El resultado de la operación es: {response.result}")