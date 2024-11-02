#!/usr/bin/python3
#puerto 1234 ip: 192.168.8.224
import sys
import socket
import exercise_pb2

if len(sys.argv) < 2:
    print ('Usage: ./proto-client.py <host>')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
destination = (sys.argv[1], 1234)

student = 'Angela.Jiao'
#Construimos la instancia de lo que queremos enviar
request = exercise_pb2.StudentMessage()
request.type = 1
request.student_id = student

#Serializamos el mensaje para mandarlo
data = request.SerializeToString()
print(data)

sock.sendto(data,destination)

response = exercise_pb2.ServerResponse()
#recibimos el mensaje
result, server = sock.recvfrom(1024)
#deserializamos el mensaje
response.ParseFromString(result)
colors = response.colors
count = len(colors)

request2 = exercise_pb2.StudentMessage()
#indicamos que ahora es de tipo 2
request2.type = 2
request2.student_id = student
request2.result = count
#serializamos el mensaje para mandarlo
data = request2.SerializeToString()
sock.sendto(data, destination)
sock.close()



