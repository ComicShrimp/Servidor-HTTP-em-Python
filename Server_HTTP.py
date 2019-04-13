# Código para um simples servidor HTTP

import http.server
import socketserver

PORT = 8080
IP = "127.0.0.1"

Handler = http.server.SimpleHTTPRequestHandler

Server_http = socketserver.TCPServer((IP, PORT), Handler)
print("Servidor na Porta", PORT)
Server_http.serve_forever()
