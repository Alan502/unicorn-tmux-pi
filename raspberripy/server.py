from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer


class S(BaseHTTPRequestHandler):
    """unicorn tmux pi webserver, serves the routes that control the unicorn phat through http
    """

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        # server reports itself on any get request
        self.wfile.write("i am unicorn tmux pi\n")
        self.wfile.write("https://github.com/Alan502/unicorn-tmux-pi\n")

    def do_POST(self):
        self._set_headers()
        print self.rfile
        self.wfile.write(self.rfile)


def run(server_class=HTTPServer, handler_class=S, port=61002):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'unicorn tmux pi running...'
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        # if a port is provided as an argument, run the server on this port.
        run(port=int(argv[1]))
    else:
        run()
