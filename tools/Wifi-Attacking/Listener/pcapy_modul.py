import pcapy

def start_pcapy_listener(interface='eth0'):
    print(f'Starting pcapy listener on {interface}')
    
    cap = pcapy.open_live(interface, 65536, True, 0)
    
    def packet_callback(header, packet):
        print(f'Packet captured: {packet}')
    
    cap.loop(0, packet_callback)