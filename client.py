import socket


class TCPclient():
    def __init__(self, sms):
        self.target_ip = 'localhost'
        self.target_port = 8888
        self.send_and_recv_data: dict = {}
        self.send_and_recv_data.update({len(self.send_and_recv_data): sms})
        self.client_sms: bytes = bytes(sms, "utf-8")

    def run_client(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.target_ip, self.target_port))

        client.send(self.client_sms)
        recv_from_server = client.recv(1024)
        recv_sms = recv_from_server.decode("utf-8")
        self.send_and_recv_data.update({len(self.send_and_recv_data): recv_sms})

        print("Get Back Data From Server: ", recv_sms)
        client.close()


if __name__ == "__main__":
    while True:
        sms: str = input("Enter something to send: ")
        tcp_client = TCPclient(sms)
        tcp_client.run_client()
