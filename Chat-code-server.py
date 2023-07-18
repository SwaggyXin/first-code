import socket
import threading

def handle_client(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        if message == "quit":
            break
        print("Received message:", message)
        response = input("Enter your response: ")
        client_socket.send(response.encode())
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen()

    print("Server started. Waiting for connections...")

    while True:
        client_socket, addr = server_socket.accept()
        print('Connected to', addr)
        threading.Thread(target=handle_client, args=(client_socket,)).start()

start_server()

