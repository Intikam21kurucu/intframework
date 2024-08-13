from socket_modul import start_socket_listener
from pysnmp_modul import start_pysnmp_listener
from pcapy_modul import start_pcapy_listener
import threading

def main():
    # Socket ile dinleme başlat
    socket_thread = threading.Thread(target=start_socket_listener, args=('0.0.0.0', 12345))
    socket_thread.start()
    
    # PySNMP ile dinleme başlat
    pysnmp_thread = threading.Thread(target=start_pysnmp_listener, args=('public', 161))
    pysnmp_thread.start()
    
    # Pcapy ile dinleme başlat
    pcapy_thread = threading.Thread(target=start_pcapy_listener, args=('eth0',))
    pcapy_thread.start()

if __name__ == '__main__':
    main()