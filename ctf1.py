import socket

HOST = '0.0.0.0' 
PORT = 51116     
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(15)
while 1:
    conn, addr = s.accept()
    key = "Your key is: f8ed6029b733f53260eeaee72529636475a8140640e260aef7c0054a9c9338b0\n"
    conn.sendall(key)
    conn.close()
