import socket

HOST = ''      # Empty string to bind to all available interfaces
PORT = 5000

# Create a socket object with IPv4 as address family and TCP as connection
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    print('Socket successfully created!')

    # Bind the socket to the port
    server_socket.bind((HOST, PORT))

    # Listen for incoming connections, queue up to 1 connection
    server_socket.listen(1)
    print(f"Socket is listening on port: {PORT}...")

    while True:
        try:
            # Accept a new connection
            client_socket, client_address = server_socket.accept()
            with client_socket:  # Use context manager to ensure client socket closes after use
                print(f"Connection established with {client_address}")

                while True:
                    # Receive message from client (up to 1024 bytes)
                    client_message = client_socket.recv(1024).decode()

                    if client_message == 'q':
                        print('Goodbye, closing the connection...')
                        server_socket.close()
                        break

                    print(f"Message from client: {client_message}")

                    # Send a response back to the client
                    response = input('Enter response to send to client: ')
                    client_socket.sendall(response.encode())

        except Exception as e:
            print(f"An error occurred: {e}")
            break
