from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR


class SocketServer:
    def __init__(self, port: int = 8080, address: str = "localhost") -> None:
        self.backlog_length = 5
        self.host_port = port
        self.host_address = address
        self.server_address = (self.host_address, self.host_port)
        self.connection_buff_size = 1024

    def create_connection(self):
        # Here we create a TCP/IP socket
        # AF_INET indicates that we are using IPv4
        # SOCK_STREAM indicates that we are using TCP
        server = socket(AF_INET, SOCK_STREAM)

        server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

        # If we wanted to create a UDP socket instead, we would use SOCK_DGRAM
        # server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # We are indicating the host address and the host port.
        server.bind(self.server_address)

        # Here we are making our server to listen to 5 connection each time.
        server.listen(self.backlog_length)

        print(f"Server listening in {self.host_address}:{self.host_port}...")

        """ 
        Now we are prepared to connect, with the method accept we create a 'conn' value, that means that we 
        have a private connection between oour mainly socket (server) and the ohter host that is reaching our server,
        and the variable 'address' is the address bound to the socket on the other end of the connection.
        """
        conn, address = server.accept()

        print(f"Connected by: {address}")

        data = conn.recv(self.connection_buff_size)

        print("-------------- Decoding message received --------------", end="\n")
        print(f"Decoded message: {data.decode()}")

        send_message_in_bytes = "Message received successfully".encode()
        conn.send(send_message_in_bytes)

        conn.close()


if __name__ == "__main__":
    server = SocketServer()
    server.create_connection()
