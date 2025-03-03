from flask import Flask, request, jsonify, send_file, url_for, render_template
from flask_cors import CORS
from pytubefix import YouTube
import os
import shutil
import time
import threading
import hmac
import hashlib
import base64
import unicodedata
import re


app = Flask(__name__)
CORS(app)

DOWNLOAD_FOLDER = "downloads"
SECRET_KEY = "YTDOWN2025SGD"  # Cambia esto por una clave segura
EXPIRATION_TIME = 300  # 5 minutos

os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def generar_firma(filename, expiration):
    """Genera una firma HMAC para validar la URL de descarga."""
    mensaje = f"{filename}:{expiration}"
    firma = hmac.new(SECRET_KEY.encode(), mensaje.encode(), hashlib.sha256).digest()
    return base64.urlsafe_b64encode(firma).decode()
def limpiar_nombre_archivo(nombre):
    """Elimina caracteres Unicode y especiales del nombre del archivo."""
    nombre = unicodedata.normalize("NFKD", nombre).encode("ascii", "ignore").decode("ascii")
    nombre = re.sub(r"[^\w\s.-]", "", nombre)  # Eliminar cualquier carácter extraño
    return nombre

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/download', methods=['POST'])
def download_video():
    data = request.json
    url = data.get("url")
    solo_audio = data.get("solo_audio", False)

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        yt = YouTube(url, 'ANDROID')
        if solo_audio:
            stream = yt.streams.get_audio_only()
            filename = f"{yt.title}.mp3"
        else:
            stream = yt.streams.get_highest_resolution()
            filename = f"{yt.title}.mp4"

        file_path = os.path.join(DOWNLOAD_FOLDER, filename)
        stream.download(output_path=DOWNLOAD_FOLDER, filename=filename)

        # 🔹 Generar una URL con firma y expiración
        expiration = int(time.time()) + EXPIRATION_TIME
        signature = generar_firma(filename, expiration)
        download_url = url_for('get_file', filename=filename, expiration=expiration, signature=signature, _external=True)

        return jsonify({"download_url": download_url})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/file/<filename>', methods=['GET'])
def get_file(filename):
    file_path = os.path.join(DOWNLOAD_FOLDER, filename)

    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404

    response = send_file(file_path, as_attachment=True)

    # 🔹 Iniciar un hilo en segundo plano para borrar el archivo DESPUÉS de la descarga
    threading.Thread(target=borrar_archivo_seguro, args=(file_path, 60), daemon=True).start()

    return response

def borrar_archivo_seguro(file_path, delay=60):
    """Espera X segundos y borra el archivo SOLO si ya no está en uso."""
    time.sleep(delay)
    try:
        if os.path.exists(file_path):
            # Intenta abrir el archivo en modo lectura para ver si está en uso
            with open(file_path, "r"):
                pass
            os.remove(file_path)
            print(f"🗑️ Archivo eliminado después de la descarga: {file_path}")
    except PermissionError:
        print(f"⏳ Archivo aún en uso, se intentará más tarde: {file_path}")
        # Si el archivo sigue en uso, intenta de nuevo en 30s
        threading.Thread(target=borrar_archivo_seguro, args=(file_path, 30), daemon=True).start()
    except Exception as e:
        print(f"❌ Error al eliminar archivo: {e}")

if __name__ == '__main__':
    app.run(debug=True)
