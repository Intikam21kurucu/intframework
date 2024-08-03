import argparse
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from pyngrok import ngrok

class ProxyHTTPRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.target_url = kwargs.pop('target_url', None)
        super().__init__(*args, **kwargs)

    def do_GET(self):
        if self.target_url:
            try:
                response = requests.get(self.target_url)
                self.send_response(response.status_code)
                self.send_header('Content-type', response.headers.get('Content-Type', 'text/html'))
                self.end_headers()
                self.wfile.write(response.content)
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"Error fetching content.")
        else:
            self.send_error(404, "File not found")

def run_server(port, target_url):
    handler = lambda *args, **kwargs: ProxyHTTPRequestHandler(*args, target_url=target_url, **kwargs)
    httpd = HTTPServer(('', port), handler)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

def main():
    parser = argparse.ArgumentParser(description="intphisher [options]")
    parser.add_argument('url', type=str, help="The URL to fetch and display.")
    args = parser.parse_args()

    # Start local server
    port = 8000
    run_server(port, args.url)

    # Create an ngrok tunnel
    public_url = ngrok.connect(port)
    print(f"Ngrok tunnel \"{public_url}\" -> \"http://localhost:{port}\"")

if __name__ == "__main__":
    main()