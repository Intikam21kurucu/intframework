import requests
from geopy.geocoders import Nominatim
import folium

def get_location_by_ip(ip_address):
    try:
        # IP adresi ile coğrafi konum bilgisi almak için bir API kullan
        response = requests.get(f'http://ip-api.com/json/{ip_address}')
        data = response.json()

        if data['status'] == 'fail':
            print("[!] Unable to get location data for this IP address.")
            return None
        else:
            return data['lat'], data['lon']
    except Exception as e:
        print(f"[!] Error: {e}")
        return None

def display_map(latitude, longitude):
    # Harita oluştur
    map = folium.Map(location=[latitude, longitude], zoom_start=12)
    
    # Kullanıcının konumunu işaretle
    folium.Marker([latitude, longitude], popup="Target Location").add_to(map)
    
    # Haritayı HTML dosyasına kaydet
    map.save("location_map.html")
    print("Harita 'location_map.html' olarak kaydedildi.")

if __name__ == "__main__":
    modul_adi = "location_tracker"
    aciklama = "Enter ip"
    
    # Kullanıcıdan IP adresi al
    ip_address = input(f"\033[91mint4 {modul_adi}[{aciklama}] > \033[0m")
    
    if ip_address:
        location = get_location_by_ip(ip_address)
        
        if location:
            latitude, longitude = location
            display_map(latitude, longitude)
        else:
            print("[!] Geçersiz IP adresi veya veri alınamadı.")
    else:
        print("[!] Lütfen geçerli bir IP adresi girin.")