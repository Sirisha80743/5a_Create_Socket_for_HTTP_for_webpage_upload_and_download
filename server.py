import socket
import random

s = socket.socket()
s.bind(('localhost', 8080))
s.listen(1)
print("Server listening...")

conn, addr = s.accept()
print("Connected from:", addr)

while True:
    data = conn.recv(1024).decode()
    if not data or data.lower() == 'exit':
        break

    print("Received:", data)
    # Randomly simulate ACK or NACK
    ack = "ACK" if random.choice([True, False]) else "NACK"
    conn.send(ack.encode())

conn.close()
s.close()
print("Server closed.")