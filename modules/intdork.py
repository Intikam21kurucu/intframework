#!/usr/bin/env python3
import argparse
from googlesearch import search

def perform_google_dork_search():
    parser = argparse.ArgumentParser( description="intdork [arguments]")
    parser.add_argument("-s", "--site", required=True, help="Aranacak site veya alan adı (Örnek: example.com)")
    parser.add_argument("-t", "--type", default="pdf", help="Dosya türü (filetype) filtresi (Varsayılan: pdf)")
    parser.add_argument("-i", "--intitle", help="Başlıkta arama yap")
    parser.add_argument("-u", "--inurl", help="URL'de arama yap")
    parser.add_argument("-n", "--num_results", type=int, default=10, help="Dönecek sonuç sayısı (Varsayılan: 10)")
    
    args = parser.parse_args()
    
    # Google dork sorguları
    queries = []
    queries.append(f"site:{args.site} filetype:{args.type}")
    if args.intitle:
        queries.append(f"intitle:{args.intitle}")
    if args.inurl:
        queries.append(f"inurl:{args.inurl}")
    
    results = ""
    for query in queries:
        results += google_dork_search(query, args.num_results)
    
    # Sonuçları ekrana yazdırır
    print(results)

def google_dork_search(query, num_results=10):
    results = search(query, num_results=num_results)
    
    if not results:
        return "Sonuç bulunamadı.\n"
    
    result_str = f"Sorgu: {query}\n"
    for idx, result in enumerate(results, start=1):
        result_str += f"Sonuç {idx}: {result}\n"
    
    return result_str + "\n"

# Modül olarak kullanılabilir
if __name__ == "__main__":
    perform_google_dork_search()