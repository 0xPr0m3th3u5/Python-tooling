import socket

host = "0.0.0.0"
port = 9999


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(5)
    print(f"Listening on {host}:{port}")
    
    conn, addr = server.accept()
    with conn:
        print("Connection from:", addr)
        data = conn.recv(1024)
        print("Received:", data.decode(errors="replace"))
        conn.sendal(b"Hello from server\n")