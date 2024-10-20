import requests

def admin_finder(target_url):
    admin_paths = [
        "/admin",
        "/admin/login",
        "/administrator",
        "/admin.php",
        "/login.php",
        "/wp-admin",
        "/user/login",
        "/controlpanel",
        "/login",
        "/admin_area",
    ]
    
    found_admins = []
    
    for path in admin_paths:
        url = target_url + path
        response = requests.get(url)

        if response.status_code == 200:
            print(f"Bulundu: {url}")
            found_admins.append(url)
    
    if not found_admins:
        print("Yönetici paneli bulunamadı.")
    
    return found_admins

# Kullanım örneği
target_url = "http://example.com"
admin_finder(target_url)