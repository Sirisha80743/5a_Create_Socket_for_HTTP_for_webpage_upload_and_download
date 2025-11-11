import socket

c = socket.socket()
c.connect(('localhost', 8080))

n = int(input("Enter number of frames to send: "))

for i in range(n):
    frame = f"Frame {i+1}"
    c.send(frame.encode())
    ack = c.recv(1024).decode()
    print(f"Server reply for {frame}: {ack}")
    if ack == "NACK":
        print("Resending frame...")
        c.send(frame.encode())
        print("Resent:", c.recv(1024).decode())

c.send(b"exit")
c.close()
print("Client closed.")