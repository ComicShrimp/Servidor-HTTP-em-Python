from http.server import  HTTPServer, BaseHTTPRequestHandler
import os

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'

        try:
            file = open(os.curdir + os.sep + self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(file.read().encode())
            file.close()

        except IOError:
            self.send_error(404, 'File Not Found: {}'.format(self.path))

