from socket import socket, AF_INET, SOCK_STREAM


class SocketClient:
    def __init__(self, port: int = 8080, address: str = "localhost") -> None:
        self.backlog_length = 5
        self.host_port = port
        self.host_address = address
        self.server_address = (self.host_address, self.host_port)
        self.connection_buff_size = 1024

    def connect_to_server(
        self,
    ):
        try:
            client = socket(AF_INET, SOCK_STREAM)
            client.connect(self.server_address)

            send_message_in_bytes = "Hello Server!".encode()
            client.send(send_message_in_bytes)

            data = client.recv(self.connection_buff_size)

            print(f"Message received: {data}", end="\n")
        except ConnectionRefusedError:
            print(f"Refused connection with {self.server_address}!")


if __name__ == "__main__":
    client = SocketClient()
    client.connect_to_server()
