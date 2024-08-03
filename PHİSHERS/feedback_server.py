from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

class FeedbackHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('feedback_form.html', 'r') as file:
                self.wfile.write(file.read().encode('utf-8'))
        else:
            self.send_error(404, "File not found")

    def do_POST(self):
        if self.path == '/submit_feedback':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(post_data)
            
            name = form_data.get('name', [''])[0]
            feedback = form_data.get('feedback', [''])[0]
            
            with open('feedback.txt', 'a') as file:
                file.write(f"Name: {name}\n")
                file.write(f"Feedback: {feedback}\n")
                file.write("-" * 40 + "\n")
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Thank you for your feedback!")
        else:
            self.send_error(404, "File not found")

def run_server(port):
    httpd = HTTPServer(('', port), FeedbackHandler)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server(8000)