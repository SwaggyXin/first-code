import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    while True:
        message = input("Enter your message: ")
        client_socket.send(message.encode())
        if message == "quit":
            break
        response = client_socket.recv(1024).decode()
        print("Received response:", response)

    client_socket.close()

start_client()
