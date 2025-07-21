import socket
from typing import Optional

CONFIG = {
    "LHOST": "0.0.0.0",
    "LPORT": 4444,            # Başlangıç portu, sonrasında otomatik güncellenecek
    "BUFFER_SIZE": 4096,
    "TIMEOUT": 5,
    "MAX_SESSIONS": 100
}

def is_port_free(host: str, port: int, timeout: float = 1.0) -> bool:
    """
    Verilen host ve port için portun kullanılabilir olup olmadığını kontrol eder.
    Port kullanılmıyorsa True, doluysa False döner.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        try:
            result = sock.connect_ex((host, port))
            return result != 0
        except Exception:
            # Hata varsa portun dolu olmadığını varsay
            return True

def find_free_port(start_port: int = 4444, max_ports: int = 100, host: Optional[str] = None) -> int:
    """
    start_port'tan başlayarak max_ports kadar portu kontrol eder.
    İlk boş portu bulup döner, bulunamazsa -1 döner.
    """
    host = host or CONFIG["LHOST"]
    for port in range(start_port, start_port + max_ports):
        if is_port_free(host, port):
            return port
    return -1

def update_config_port(config: dict, start_port: int = 4444, max_ports: int = 100) -> dict:
    """
    CONFIG sözlüğündeki LPORT değerini kullanılabilir ilk port ile günceller.
    Eğer uygun port bulunamazsa RuntimeError fırlatır.
    """
    free_port = find_free_port(start_port, max_ports, config.get("LHOST", "0.0.0.0"))
    if free_port == -1:
        raise RuntimeError(f"{max_ports} port içinde boş port bulunamadı./ Not found port")
    config["LPORT"] = free_port
    return config

# CONFIG'u dinamik kullanılabilir port ile güncelle
try:
    CONFIG = update_config_port(CONFIG, 4444, 100)
except RuntimeError as e:
    print(f"[config.py] Error: {e}")