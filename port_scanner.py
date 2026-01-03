from socket import socket, AF_INET, SOCK_STREAM, timeout


class PortScanner:
    def __init__(
        self, end_port: int, start_port: int = 0, timeout: float = 0.5
    ) -> None:
        self.port_range = range(start_port, end_port)
        self.timeout = timeout

    def scan(self, url: str):
        print(f"SCANNING {url} IN PORTS {self.port_range}...", end="\n")

        for port in self.port_range:
            scanner_socket = None
            print(f"Checking for port {port}", end="\n")
            try:
                scanner_socket = socket(AF_INET, SOCK_STREAM)
                scanner_socket.settimeout(self.timeout)
                scanner_socket.connect((url, port))

                print(f"[+] SUCCESS: Port {port} is open!", end="\n\n")
            except (ConnectionRefusedError, timeout):
                pass
            except Exception as e:
                print(f"Error with port {port}: {e}")
            finally:
                if scanner_socket:
                    scanner_socket.close()


if __name__ == "__main__":
    scanner = PortScanner(85, start_port=78)
    scanner.scan("scanme.nmap.org")
