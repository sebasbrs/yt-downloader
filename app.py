from flask import Flask, request, jsonify, Response
from pytubefix import YouTube
import os

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download_video():
    data = request.json
    url = data.get("url")
    solo_audio = data.get("solo_audio", False)

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        yt = YouTube(url, 'MWEB')
        if solo_audio:
            ys = yt.streams.get_audio_only()
        else:
            ys = yt.streams.get_highest_resolution()

        def generate():
            with ys.stream() as stream:
                while chunk := stream.read(1024 * 1024):  # Lee en bloques de 1MB
                    yield chunk

        filename = f"{yt.title}.{'mp3' if solo_audio else 'mp4'}"
        content_type = "audio/mpeg" if solo_audio else "video/mp4"

        return Response(generate(), content_type=content_type, headers={
            "Content-Disposition": f"attachment; filename={filename}"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
