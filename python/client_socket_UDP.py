# UDP client

import socket

target_host = "127.0.0.1"
target_port = 9997

with socket.socket(socket.AF_INET, socket.DGRAM) as s :
    s.sendto(b"AAABBBCCC", (target_host, target_port))
    
data, addr = s.recvfrom(4096)

print(data.decode())
s.close()

# Creating socket object -> sendto() -> recvfrom()