# TCP SOCKET

It is the one which is the most used for offensive scripting

### Creating Socket
```
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
Telling the OS:
- IPv4
- stream-based transport / TCP endpoint

### Connect

``` 
s.connect(("<ip address>", <port>))
```

The OS:
- chooses a local ephemeral port
- looks up the route
- may resolve the DNS first if used a hostname
- performs three way handshake.

> NOTE: `connect()` does not send your data

### Send bytes

```
s.sendall(b"GET / HTTP/1.1\r\nHost: target\r\n\r\n")
```

Your bytes go into **kernel's send buffer**

the kernel:
- splits them into TCP segments
- adds TCP/ip headers
- handles retransmission if packtes are lost
- deals with congestion control
- handles the packet to the NIC

### Receive Bytes

```
data = s.recv(4096)
```

The kernel receives the packets from the network and places the payload into the **Receive buffer**.

Then `recv()` copies some of those bytes from kernel space into your python process.

> recv(4096) means "Up to 4096 bytes"

### close

```
s.close()
```

The kernel tears down the connection, usually with TCP FIN/ACK behavior.


