# TCP Client in python

import socket

host = "example.com"
port = 80

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s :
    s.settimeout(5)
    s.connect((host, port))
    
    request = (
        "GET / HTTP/1.1\r\n"
        "Host : example.com\r\n"
        "Connection: close\r\n"
        "\r\n"
    )
    s.sendall(request.encode())
    
    response = b""
    while True:
        chunk = s.recv(4096)
        if not chunk:
            break
        response += chunk
        
print(response.decode(errors="replace"))
s.close()
# Create a socket object > connect > send data > Receive data > close the socket



