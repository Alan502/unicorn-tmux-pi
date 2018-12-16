from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import unicornhat as unicorn
from game_of_life import GameOfLife
import time

r_shift = 0
g_shift = 0
b_shift = 0
life = GameOfLife(r_shift, g_shift, b_shift)


def run_unicorn_loop():
    global life
    life.next_generation()
    life.show_board()
    if life.all_dead():
        life = GameOfLife(r_shift, g_shift, b_shift)


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
        global life
        global r_shift
        global g_shift
        global b_shift
        self._set_headers()
        content_length = int(self.headers['Content-length'])
        in_text = self.rfile.read(content_length)
        if in_text.startswith('gameoflife'):
            r_shift = int(in_text[11])
            g_shift = int(in_text[13])
            b_shift = int(in_text[15])
            life = GameOfLife(r_shift, g_shift, b_shift)
        if in_text.startswith('random'):
            pass
        self.wfile.write(in_text)


def run(server_class=HTTPServer, handler_class=S, port=61002):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'unicorn tmux pi running...'
    httpd.timeout = 1
    httpd.handle_timeout = run_unicorn_loop
    while True:
        httpd.handle_request()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        # if a port is provided as an argument, run the server on this port.
        run(port=int(argv[1]))
    else:
        run()
