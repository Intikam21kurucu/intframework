#!/usr/bin/env python3
import argparse
import requests
from bs4 import BeautifulSoup

class BingEngine:
    def __init__(self, query, limit=3, count=50):
        self.query = query
        self.limit = limit
        self.count = count
        self.emails = []

    def run_crawl(self):
        # Bing'de sorgu yap ve sonuçları topla
        url = f'https://www.bing.com/search?q={self.query}&count={self.count}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('a', href=True)
        
        for result in results:
            if '@' in result['href']:
                self.emails.append(result['href'])

class EmailSearch:
    def __init__(self):
        self.EMAILS = []

    def search(self, query, engines, limit=3, count=50, key=None, thread=2):
        # Burada belirtilen motorlar ve seçeneklerle e-posta arama mantığını gerçekleştirin
        for engine in engines:
            if engine.lower() == 'bing':
                bing = BingEngine(query, limit, count)
                bing.run_crawl()
                self.EMAILS.extend(bing.emails)
            # Buraya başka arama motorları da eklenebilir

    def module_api(self, args):
        # argparse namespace'den argümanları çıkarın ve aramayı gerçekleştirin
        query = args.query
        limit = args.limit
        count = args.count
        engines = args.engines.split(',')
        key = args.key
        
        # search metodunu, ayrıştırılmış argümanlarla çağırın
        self.search(query, engines, limit, count, key, args.thread)
        
        # Toplanan e-postaları döndürün
        output = {'emails': list(set(self.EMAILS))}
        return output

    def module_run(self, args):
        # Argparse tarafından ayrıştırılan argümanlara dayalı olarak modülü çalıştırma noktası
        results = self.module_api(args)
        self.alert_results(results)

    def alert_results(self, results):
        # Sonuçları bildirme veya işleme yöntemi
        print("Sonuçlar:", results)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Açık kaynaklarda e-posta aramak için.')
    parser.add_argument('-q', '--query', required=True, help='Alan adı veya şirket adı')
    parser.add_argument('-l', '--limit', type=int, default=3, help='Arama limiti (varsayılan=3)')
    parser.add_argument('-c', '--count', type=int, default=50, help='Sayfa başına sonuç sayısı (min=10, max=100, varsayılan=50)')
    parser.add_argument('-e', '--engines', required=True, help='Arama motoru adları. örn: bing,google,..')
    parser.add_argument('-k', '--key', help='Geçerli bir hunter API anahtarı verin')
    parser.add_argument('-t', '--thread', type=int, default=2, help='Her turda çalıştırılacak motor sayısı (varsayılan=2)')
    
    args = parser.parse_args()
    
    searcher = EmailSearch()
    searcher.module_run(args)