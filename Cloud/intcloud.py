from flask import Flask, request, redirect, url_for, send_from_directory, render_template, flash, session
import os
import shutil
from flask_babel import Babel, _

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = './translations'

babel = Babel(app)

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def get_locale():
    # Dil tercihini oturumdan al
    return session.get('lang', 'en')

@app.route('/set_lang/<lang>')
def set_lang(lang):
    # Kullanıcı dil tercihini ayarla
    session['lang'] = lang
    return redirect(url_for('index'))

@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('cloud_index.html', files=files)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            flash(_('File successfully uploaded'))
            return redirect(url_for('index'))
    return render_template('cloud_upload.html')

@app.route('/copy/<filename>', methods=['GET', 'POST'])
def copy_file(filename):
    if request.method == 'POST':
        target_folder = request.form['target_folder']
        source_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.exists(source_path):
            shutil.copy(source_path, target_folder)
            flash(_('File successfully copied'))
            return redirect(url_for('index'))
    return render_template('cloud_copy.html', filename=filename)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/delete/<filename>')
def delete_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        flash(_('File successfully deleted'))
    return redirect(url_for('index'))


"""
intcloud/
├── intcloud.py
├── static/
│   ├── styles.css
│   └── scripts.js
└── templates/
    ├── cloud_index.html
    ├── cloud_upload.html
    └── cloud_copy.html
"""


if __name__ == '__main__':
    app.run(debug=True)