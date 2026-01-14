import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 12345

server.bind((host, port))
server.listen(1)

print("Server started...")
conn, addr = server.accept()
print("Client connected:", addr)

while True:
    client_msg = conn.recv(1024).decode()
    if client_msg.lower() == "exit":
        print("Client left the chat.")
        break

    print("Client:", client_msg)
    msg = input("You: ")
    conn.send(msg.encode())

conn.close()
server.close()
