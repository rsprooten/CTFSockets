import os
import socket
import threading
import socketserver

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        banner = bytes("What do you want?\n", 'ascii')
        mainKey = bytes("The key is: 1f96634d3c1673a65c322c4dc20aec09fdd96abee1061ac6a0b1390dee7d2f49\n", 'ascii')
        while 1:
            try:
                self.request.sendall(bytes(banner))
                data = str(self.request.recv(1024), 'ascii')
                if "key" in data.lower():
                    response = mainKey
                elif "ls" in data.lower() or "pwd" in data.lower():
                    uitvoer = str(os.popen(data.lower()).read())
                    response = bytes(uitvoer,'ascii')
                else:
                    response = banner
                self.request.sendall(response)
            except BrokenPipeError:
                break

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 13166

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()
