import argparse
from http.server import BaseHTTPRequestHandler, HTTPServer

class RedirectAndLogIPHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.redirect_url = kwargs.pop('redirect_url', None)
        super().__init__(*args, **kwargs)

    def do_GET(self):
        # IP adresini al
        ip_address = self.client_address[0]
        
        # IP adresini log dosyasına yaz
        with open('logged_ips.txt', 'a') as file:
            file.write(f"{ip_address}\n")
        
        # Kullanıcıyı yönlendir
        self.send_response(302)
        self.send_header('Location', self.redirect_url)
        self.end_headers()

def run_server(port, redirect_url):
    handler = lambda *args, **kwargs: RedirectAndLogIPHandler(*args, redirect_url=redirect_url, **kwargs)
    server_address = ('', port)
    httpd = HTTPServer(server_address, handler)
    print(f"Starting server on port {port} and redirecting to {redirect_url}...")
    httpd.serve_forever()

def main():
    parser = argparse.ArgumentParser(description="router")
    parser.add_argument('--port', type=int, default=8000, help='Port to run the server on (default: 8000)')
    parser.add_argument('--url', type=str, required=True, help='URL to redirect users to')

    args = parser.parse_args()
    
    run_server(args.port, args.url)

if __name__ == "__main__":
    main()