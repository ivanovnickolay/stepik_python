import socket
req = 'Hello'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# связываем с адресом и портом
s.connect(('127.0.0.1', 1234))
#
s.send(req.encode())
rsv = s.recv(1024)
s.close()
print(rsv)