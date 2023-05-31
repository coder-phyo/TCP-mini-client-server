import socket
import  subprocess

class TcpServer():

    def __init__(self):
        self.server_ip = "localhost"
        self.server_port = 8888
        self.save: dict = {}

    def main(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.server_ip, self.server_port))
        server.listen()
        print("Server listen on ip:{} and port:{}".format(self.server_ip, self.server_port))

        try:
            while True:
                client, address = server.accept()
                print("Accepted Connection from  - {}:{}".format(address[0], address[1]))
                self.handle_client(client)
        except Exception as err:
            print(err)

    def handle_client(self, client_socked):
        with client_socked as sock:
            from_client = sock.recv(1024)
            print("Received Data from client:", from_client.decode("utf-8"))
            received_data = from_client.decode("utf-8")

            # test back door
            # print("Running Comment: ",received_data)
            # output = subprocess.getoutput(received_data)
            # print("***********\n",output)
            # print("*************")


            message = "Server got it:>" + received_data
            to_send = bytes(message, "utf-8")
            sock.send(to_send)


if __name__ == "__main__":
    tcpserver = TcpServer()
    tcpserver.main()
