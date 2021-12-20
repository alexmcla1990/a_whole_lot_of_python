import socket

#connects to our server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("same ipaddress", 54321))
print("connection established to server")
sock.close()

message = sock.recv(1024)
print(message)
result = "hello"
sock.send(result)
sock.close()