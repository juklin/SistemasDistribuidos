import socket

target_host = 'localhost'
target_port = 1314

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))
client.send('Eu sou o cliente, estou me conectando ao servidor.')

resposta = client.recv(4096)
print (resposta)