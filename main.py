from flask import Flask, render_template

app = Flask(__name__)

# Ana sayfa route'u
@app.route('/')
def home():
    return render_template('menu.html')

# İletişim sayfası route'u
@app.route('/contact')
def contact():
    return render_template('contact.html')

# DNS Lookup sayfası
@app.route('/dns_lookup')
def dns_lookup():
    return render_template('dns_lookup.html')

# Subdomain Lookup sayfası
@app.route('/subdomain_lookup')
def subdomain_lookup():
    return render_template('subdomain_lookup.html')

# Nmap sayfası
@app.route('/nmap')
def nmap():
    return render_template('nmap.html')

# Dokümanlar sayfası
@app.route('/docs')
def docs():
    return render_template('docs.html')

# İndir sayfası
@app.route('/download')
def download():
    return render_template('download.html')

# Gizlilik politikası sayfası
@app.route('/privacy_policy')
def privacy_policy():
    return render_template('privacy_policy.html')

# Used Services sayfası
@app.route('/used_services')
def used_services():
    return render_template('used_services.html')

# Whois geçmişi sayfası
@app.route('/whois_history')
def whois_history():
    return render_template('whois_history.html')

# Menü sayfası
@app.route('/menu')
def menu():
    return render_template('menu.html')

if __name__ == "__main__":
    app.run(debug=True)