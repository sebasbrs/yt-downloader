from flask import Flask, request, jsonify, redirect
from pytubefix import YouTube

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download_video():
    data = request.json
    url = data.get("url")
    solo_audio = data.get("solo_audio", False)

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        yt = YouTube(url, 'ANDROID')  # Cambiamos 'MWEB' a 'ANDROID' para evitar el error del PoToken
        if solo_audio:
            stream = yt.streams.get_audio_only()
        else:
            stream = yt.streams.get_highest_resolution()

        # Redirigir al usuario a la URL directa del archivo en YouTube
        return jsonify({"download_url": stream.url})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
