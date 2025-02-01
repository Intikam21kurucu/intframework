from flask import Flask, render_template_string

# Flask uygulamasını başlat
app = Flask(__name__)

# Ana sayfa (menu.html) için rota
@app.route('/')
def home():
    # 'menu.html' dosyasını doğrudan okuma
    with open('menu.html', 'r') as file:
        html_content = file.read()
    return render_template_string(html_content)

# Uygulamayı çalıştır
if __name__ == '__main__':
    app.run(debug=True)