import socket
import threading

# List to hold connected clients
clients = []

def handle_client(client, addr):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            break

def broadcast(message):
    for client in clients:
        try:
            client.send(message.encode('utf-8'))
        except:
            continue

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5555))
    server.listen()

    print("Server is running...")
    
    while True:
        client, addr = server.accept()
        clients.append(client)
        print(f"Connected with {addr}")
        thread = threading.Thread(target=handle_client, args=(client, addr))
        thread.start()

start_server()
