import socket

s = socket.socket()

port = 8888

s.connect(('192.168.149.130', port))

data = s.recv(1024)

s.send(b'Hi, saya client. Terima Kasih!');

print (data)

s.close()
