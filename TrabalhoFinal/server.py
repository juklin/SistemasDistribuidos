import socket 

host = '' 
port = 7000 
addr = (host, port)

while True:

	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.bind(addr) 
	server_socket.listen(10) 
  
	print('Aguardando conexão')
  
	con, cliente = server_socket.accept() 
  
	print('Conectado')
	print("Aguardando mensagem")
  
	recebe = con.recv(1024)
  
	msg = recebe.decode()
  
	print("Mensagem recebida: " + msg)
  
	server_socket.close()

