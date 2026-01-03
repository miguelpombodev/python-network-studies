from socket import socket, AF_INET, SOCK_STREAM

client = socket(AF_INET, SOCK_STREAM)
client.connect(("localhost", 8080))

send_message_in_bytes = "Hello Server!".encode()
client.send(send_message_in_bytes)

data = client.recv(1024)

print(f"Message received: {data}", end="\n")
