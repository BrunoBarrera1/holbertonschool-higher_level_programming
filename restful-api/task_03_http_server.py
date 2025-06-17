#!/usr/bin/python3

import http.server

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        pass

    self.send_response(200)
    self.send_header("Content-Type", "application/json")
    Content-Type: text/plain
