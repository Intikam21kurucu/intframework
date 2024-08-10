from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def start_virtual_pc():
    try:
        # Tkinter uygulamasını çalıştırır
        subprocess.Popen(["python3", "İNTOFİCCİAL.py"])
        return "Virtual PC başlatıldı!"
    except Exception as e:
        return f"Bir hata oluştu: {str(e)}"

if __name__ == '__main__':
    # Flask uygulamasını başlatırken, Tkinter uygulamasını da çalıştırır
    subprocess.Popen(["python3", "İNTOFİCCİAL.py"])
    app.run(debug=True)