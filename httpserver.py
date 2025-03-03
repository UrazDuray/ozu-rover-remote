#!/usr/bin/env python3
import http.server
import socketserver
import os

# Configuration
PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))  # Current directory

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        print(f"{self.client_address[0]} - {format % args}")

# Create and start the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"HTTP Server running at http://0.0.0.0:{PORT}")
    print(f"Serving files from: {DIRECTORY}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer shutting down...")
        httpd.server_close()