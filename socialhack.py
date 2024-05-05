import requests
import os


s = input("Do you accept responsibility?")

# Instagram sayfasının URL'si
url = input("please url: ")

# İstek gönder
response = requests.get(url)

# Eğer istek başarılıysa, içeriği yazdır
if response.ok:
    content = response.text
    print(content)