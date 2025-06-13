#!/usr/bin/python3

import http.server
import socketserver
import json

class pepe(http.server.BaseHTTPRequestHandler):
    def do_GET(self):

        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {
                    "name": "bruno",
                    "age": "19",
                    "city": "pinar"
            }
            json_response = json.dumps(data)
            self.wfile.write(json_response.encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

if __name__ == "__main__":
    port = 8000
    with socketserver.TCPServer(("", port), pepe) as httpd:
        print(f"Serving on port {port}")
        httpd.serve_forever()
