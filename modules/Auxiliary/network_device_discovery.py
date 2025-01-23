#!/usr/bin/env python3
import scapy.all as scapy
import socket
import json

class NetworkDeviceDiscovery:
    """[Class for discovering devices in the local network]"""

    def __init__(self):
        """[Initialize with local network information]"""
        self.network = self.get_local_network()

    def get_local_network(self):
        """[Get local network IP address]"""
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return '.'.join(local_ip.split('.')[:-1]) + '.0/24'

    def discover_devices(self):
        """[Discover devices in the local network]"""
        arp_request = scapy.ARP(pdst=self.network)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast / arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
        
        devices = []
        for element in answered_list:
            devices.append({'IP': element[1].psrc, 'MAC': element[1].hwsrc})
        return devices

if __name__ == "__main__":
    discovery_tool = NetworkDeviceDiscovery()
    devices = discovery_tool.discover_devices()
    print(json.dumps(devices, indent=4))