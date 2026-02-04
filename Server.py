import socket
server=socket.socket()
server.bind(("localhost",12345))
server.listen()
conn,addr=server.accept()
data=conn.recv(1024).decode()
conn.send(data.encode())
