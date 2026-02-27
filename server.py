#!/usr/bin/env python3
"""
Simple HTTP server for go-trader dashboard
Serves the dashboard on port 8080 and proxies API requests to port 8099
"""
import http.server
import socketserver
import urllib.request
import json
from urllib.parse import urlparse

PORT = 8080
TRADER_API = "http://localhost:8099"

class DashboardHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Enable CORS
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_GET(self):
        # Proxy /status requests to the go-trader API
        if self.path == '/status':
            try:
                with urllib.request.urlopen(f"{TRADER_API}/status") as response:
                    data = response.read()
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(data)
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                error_data = json.dumps({"error": str(e)})
                self.wfile.write(error_data.encode())
        else:
            # Serve static files
            super().do_GET()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

if __name__ == "__main__":
    Handler = DashboardHandler
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"✅ Go-Trader Dashboard running at http://localhost:{PORT}")
        print(f"📊 Open in your browser to view trading activity")
        print(f"🔄 Auto-refreshes every 30 seconds")
        print(f"\nPress Ctrl+C to stop\n")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n👋 Dashboard stopped")
