import socket

HOST = ''  # Bind to all available interfaces
PORT = 1717

# Create a socket with IPv4 as address family and UDP as connection
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    # Bind the socket to the port
    server_socket.bind((HOST, PORT))
    print(f"Server is listening on port: {PORT}...")

    while True:
        # Receive message from client (up to 1024 bytes)
        message, client_address = server_socket.recvfrom(1024)
        print(f"Message from client {client_address}: {message.decode()}")

        if message.decode() == 'q':
            print('Goodbye, server is shutting down...')
            break

        # Send a response back to the client
        response = input('\nEnter response to send to client: ')
        server_socket.sendto(response.encode(), client_address)
        print('Responded back to client!')
