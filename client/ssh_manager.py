#!/usr/bin/python


from paramiko import client
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import sys
from sys import argv

host='raspberrypi.local'
username = 'pi'
port='61002'
password='raspberry'
connection=None

class ssh:
    client = None

    def __init__(self, address, username, password):
        print("Connecting to server.")
        self.client = client.SSHClient()
        self.client.set_missing_host_key_policy(client.AutoAddPolicy())
        self.client.connect(address, username=username, password=password, look_for_keys=False)

    def sendCommand(self, command):
        if(self.client):
            stdin, stdout, stderr = self.client.exec_command(command)
            while not stdout.channel.exit_status_ready():
                # Print data when available
                if stdout.channel.recv_ready():
                    alldata = stdout.channel.recv(1024)
                    prevdata = b"1"
                    while prevdata:
                        prevdata = stdout.channel.recv(1024)
                        alldata += prevdata

                    print str(alldata)
                    return str(alldata)
        else:
            print("Connection not opened.")


class S(BaseHTTPRequestHandler):
    """ssh manager server, interacts with raspberry pi through ssh on input
       ip address.
    """

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        # server reports itself on any get request
        self.wfile.write("i am ssh manager\n")
        self.wfile.write("https://github.com/Alan502/unicorn-tmux-pi\n")

    def do_POST(self):
        global connection
        self._set_headers()
        content_length = int(self.headers['Content-length'])
        in_text = self.rfile.read(content_length)
        self.wfile.write(connection.sendCommand(in_text))


def run(server_class=HTTPServer, handler_class=S, port=61002):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd on port %s' % port
    httpd.serve_forever()

if __name__ == "__main__":
    if len(argv) == 1:
      print "usage: ssh_manager.py <host> <username> <password> <ssh_manager_port> "
      sys.exit(1)
    if len(argv) > 1:
        host = argv[1]
    if len(argv) > 2:
        username = argv[2]
    if len(argv) > 3:
        password = argv[3]
    if len(argv) > 4:
        port = argv[4]
    connection = ssh(host, username, password)
    run(port=int(port))

