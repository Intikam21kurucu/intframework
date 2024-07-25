from flask import Flask, jsonify
from daemonize import Daemonize
import os
import time

app = Flask(__name__)

# Dosya yolu ve script
timestamp_file = "/data/data/com.termux/files/home/last_check_timestamp.txt"
script_to_run = "/data/data/com.termux/files/home/update_script.py"
pid_file = "/data/data/com.termux/files/home/flask_daemon.pid"

@app.route('/')
def index():
    current_time = time.time()

    if os.path.exists(timestamp_file):
        with open(timestamp_file, 'r') as file:
            last_check_time = float(file.read().strip())
    else:
        last_check_time = 0

    if (current_time - last_check_time) >= 172800:  # 2 gün = 172800 saniye
        os.system(f"python3 {script_to_run}")

        with open(timestamp_file, 'w') as file:
            file.write(str(current_time))
        return jsonify({'status': 'Script executed'})
    else:
        return jsonify({'status': 'No need to execute script'})

def main():
    app.run(host='0.0.0.0', port=5000)

# Daemonize ile Flask uygulamasını arka planda çalıştır
daemon = Daemonize(app="flask_daemon", pid=pid_file, action=main)
daemon.start()