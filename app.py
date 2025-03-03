import time
import threading
import os
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from pytubefix import YouTube

app = Flask(__name__)
CORS(app)

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

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

        return jsonify({"download_url": f"http://127.0.0.1:5000/file/{filename}"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

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

@app.route('/file/<filename>', methods=['GET'])
def get_file(filename):
    file_path = os.path.join(DOWNLOAD_FOLDER, filename)

    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404

    response = send_file(file_path, as_attachment=True)

    # 🔹 Iniciar un hilo en segundo plano para borrar el archivo DESPUÉS de la descarga
    threading.Thread(target=borrar_archivo_seguro, args=(file_path, 60), daemon=True).start()

    return response

if __name__ == '__main__':
    app.run(debug=True)
