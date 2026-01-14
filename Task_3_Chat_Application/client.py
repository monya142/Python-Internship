import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 12345

client.connect((host, port))
print("Connected to server")

while True:
    msg = input("You: ")
    client.send(msg.encode())

    if msg.lower() == "exit":
        print("You left the chat.")
        break

    server_msg = client.recv(1024).decode()
    print("Server:", server_msg)

client.close()
