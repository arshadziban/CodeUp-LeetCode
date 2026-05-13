import socket
import threading
import time

# Server function
def run_server():
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('localhost', 8081))
    server.listen()
    conn, addr = server.accept()
    msg = conn.recv(1024).decode()
    conn.send("accepted".encode())
    conn.close()
    server.close()


# Start server in background
threading.Thread(target=run_server, daemon=True).start()
time.sleep(1)


# Client
client = socket.socket()

try:
    client.connect(('localhost', 8081))
    print("Server connected")

    message = input("Enter your message: ")
    print() 

    client.send(message.encode())

    response = client.recv(1024).decode()
    print("Server accepted message")

    client.close()
except:
    print("Not connected")
