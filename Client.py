import socket
client=socket.socket()
client.connect(("localhost",12345))
message=input("enter massage:")
client.send(message.encode())
print("server is saying:",client.recv(1024).decode())
