#!/usr/bin/env python3
import streamlit as st
import socket
from concurrent.futures import ThreadPoolExecutor
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="Network Tool", layout="centered")
TEMPLATE_DIR = "templates"

def render_template(filename, **kwargs):
    path = os.path.join(TEMPLATE_DIR, filename)
    if not os.path.exists(path):
        st.error(f"{filename} bulunamadı.")
        return
    with open(path, "r", encoding="utf-8") as f:
        html_content = f.read()
    if kwargs.get("result"):
        html_content = html_content.replace("{{ result }}", kwargs["result"])
    components.html(html_content, height=800, scrolling=True)

def scan_port(port, target_ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((target_ip, port))
        return port, True
    except:
        return port, False
    finally:
        s.close()

# Menü
st.sidebar.title("Menü")
page = st.sidebar.selectbox("Sayfa", [
    "Ana Sayfa", "Nmap", "İletişim", "DNS Lookup", "Subdomain Lookup",
    "Dokümanlar", "İndir", "Gizlilik Politikası", "Kullanılan Servisler", "Whois Geçmişi"
])

if page == "Ana Sayfa":
    render_template("menu.html")

elif page == "Nmap":
    ip = st.text_input("IP Adresi")
    port_input = st.text_input("Portlar (virgülle):")
    if st.button("Taramayı Başlat"):
        if not ip:
            render_template("nmap.html", result="IP address is required.")
        else:
            ports = range(1, 65536) if not port_input else list(map(int, port_input.split(',')))
            with ThreadPoolExecutor(max_workers=100) as executor:
                results = executor.map(lambda port: scan_port(port, ip), ports)
            open_ports = [f"Port {port} is open" for port, is_open in results if is_open]
            result = "\n".join(open_ports) if open_ports else "No open ports found."
            render_template("nmap.html", result=result)
    else:
        render_template("nmap.html")

elif page == "İletişim":
    render_template("contact.html")

elif page == "DNS Lookup":
    render_template("dns_lookup.html")

elif page == "Subdomain Lookup":
    render_template("subdomain_lookup.html")

elif page == "Dokümanlar":
    render_template("docs.html")

elif page == "İndir":
    render_template("download.html")

elif page == "Gizlilik Politikası":
    render_template("privacy_policy.html")

elif page == "Kullanılan Servisler":
    render_template("used_services.html")

elif page == "Whois Geçmişi":
    render_template("whois_history.html")