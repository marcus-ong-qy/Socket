import socket
class Client:
    def __init__(self, server, port):
        # Create a Client Socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bind the socket to specified hostname and port
        self.socket.connect((server, port))
    def Request(self, request):
        if request == '':
            request = ''
        elif request[-1] != '\n':
            request += '\r\n'
        # Send Request
        self.socket.send(request)
        # Retrieve Response
        return self.socket.recv(1024)
    def close(self):
        self.socket.send('\r\n')
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print('Usage: %s [host] [server port]' %sys.argv[0])
        sys.exit(1)
    hostname = sys.argv[1]
    port = int(sys.argv[2])
    try:
        # Initiate Client
        client = Client(hostname, port)
    except:
        print('Connection not established')
        sys.exit(1)

    print(client.socket.recv(1024))
    while(1):
        request = input('') # raw_input?
        if request == 'quit':
            client.close()
            print('Connection Closed')
            exit(0)
        try:
            print(client.Request(request))
        except:
            print('Connection Broken')
            exit(1)
