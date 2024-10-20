import requests

def http_header_analyzer(target_url):
    try:
        response = requests.get(target_url)
        print(f"HTTP Başlıkları: {response.headers}")
        
        # Güvenlik kontrolleri
        if "X-Content-Type-Options" not in response.headers:
            print("Uyarı: X-Content-Type-Options başlığı eksik!")
        if "X-Frame-Options" not in response.headers:
            print("Uyarı: X-Frame-Options başlığı eksik!")
    
    except requests.exceptions.RequestException as e:
        print(f"Hata: {e}")

# Kullanım örneği
target_url = "http://example.com"
http_header_analyzer(target_url)