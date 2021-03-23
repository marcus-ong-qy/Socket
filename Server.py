import socket
import commands
import sys
class Server:
    def __init__(selfself, hostname, port):
        # Create a Server Socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Bind the socket to specified hostname and port
        self.sock.bind((hostname, port))
        # Listen to 5 clients at a time
        self.sock.listen(5)
    def Run(self):
        while(1):
            # Waiting for a request from a client.
            request, clientAddress = self.sock.accept()

            # Client Information
            print("Received a request from ", clientAddress)

            # Acknowledge the Connection
            self.sock.send("Online Calculator\nConnection Established\n")
            try:
                while(1):
                    # receive the expression
                    expression = self.sock.recv(1024)
                    try:
                        # evaluate the expression and send the output
                        request.send(eval(expression))
                    except SyntaxError:
                        # Response for wrongly formatted expression
                        request.send("Wrong Expression!")
                        pass
            except socket.error:
                print("Connection Closed")
                pass
            # Close socket
            request.shutdown(2)
            sock.close()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: %s [hostname] [port number]'%sys.argv[0])
        sys.exit(1)
    hostname = sys.argv[1]
    port = int(sys.argv[2])
    try:
        # Create Server
        server = Server(hostname, port)
    except:
        print('Server Not Created')
        sys.exit(1)
    print('Server Established')
    # Run Server
    server.Run()
