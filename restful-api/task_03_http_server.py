#!/usr/bin/python3

import http.server
import json

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            json_data = json.dumps(data)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json_data.encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("content-Type", "text/plain")
            self.end_headers()
            self
            
        elif self.path == "/info":
            info = {
                    "version": "1.0",
                    "description": "A simple API built with the http.server"
            }
            json_info = json.dumps(info)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json_info.encode("utf-8"))


        else:
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode("utf-8"))

        server_address = ('', 8000)
        https = http.server.HTTPServer(server_address, SimpleAPIHandler)

        print("Serving on port 8000...")
        httpd.serve_forever()

