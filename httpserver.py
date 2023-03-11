import http.server 
import socketserver 
import socket

PORT = 8888
Handler = http.server.CGIHTTPRequestHandler 
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("server starts on", PORT)
    httpd.serve_forever()