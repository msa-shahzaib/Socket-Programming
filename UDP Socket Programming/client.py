import socket

HOST = socket.gethostbyname(socket.gethostname())  # Local machine IP
PORT = 1717  # Same port as the server

# Create a socket with IPv4 as address family and UDP as connection
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    while True:
        message = input('\nEnter message to send to the server (q to quit): ')

        # Send the message to the server
        client_socket.sendto(message.encode(), (HOST, PORT))
        print("Message sent to server!")

        if message == 'q':
            break

        # Receive response from server (up to 1024 bytes)
        server_response, _ = client_socket.recvfrom(1024)
        print(f"Server says: {server_response.decode()}")
