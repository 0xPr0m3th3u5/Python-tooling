# Socket

## The intuition
A socket is a program's handle to a network conversation. 

[It is not the conversation itself, not the packets, not the protocol] - Just the endpoint your code uses to talk through the "Operating System"

OS layer -> The python code doesn't talk to the wire but to the OS and the OS talks to the network.

## What Socket really is?

In most systems, a socket is an OS-manaed object referenced by a *file descriptor* 

it means:
- The kernel allocates state for it
- your process gets a small integer handle
- you read/write through that handle
- the kernel moves bytes in and out of nework buffers

```s = socket.socket(...)```


## Three layers

1. Application layer

The python code decides:
- what bytes to send
- When to send
- how to parse replies

2. Transport layer
- TCP
- UDP

Decides:
- reliability
- ordering
- retransmission
- connection behavior

3. OS / Kernel layer

It handles:
- routing
- buffering
- packetization
- timeouts
- retransmission
- connection state

NOTE: The script is not doing the network itself but telling the OS to do the networking on its behalf.

