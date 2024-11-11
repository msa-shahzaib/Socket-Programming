# import the socket module
import socket

HOST = socket.gethostbyname(socket.gethostname())  # Get the local machine IP address
PORT = 5000  # Same port as the server

# Create a socket object with IPv4 address family and TCP as connection
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    try:
        # Connect to the server
        client_socket.connect((HOST, PORT))

        while True:
            # Send a message to the server
            message = input('\nEnter msg to sent to the server (q to quit): ')
            client_socket.sendall(message.encode())
            print("Message sent to server successfully!")

            if message == 'q':
                break

            # Receive and decode message from server (Upto 1024 Bytes)
            message = client_socket.recv(1024).decode()
            print(f"Server says: {message}")

    except Exception as e:
        print(f"An error occurred: {e}")
