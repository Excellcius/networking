import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Connection closed")
            break

def send_message(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5555))

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_message, args=(client,))
    send_thread.start()

start_client()
