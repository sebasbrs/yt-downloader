from werkzeug.middleware.proxy_fix import ProxyFix
from flask import Flask, request, jsonify, send_file, url_for, render_template
from flask_cors import CORS
import yt_dlp


app = Flask(__name__)

CORS(app)

app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)

### Route

@app.route('/')
def index():
    return render_template("index.html")


### Modules

@app.route('/yt-download', methods=['POST'])
def download_yt():
    data = request.json
    url = data.get("url")
    solo_audio = data.get("solo_audio", False)

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        ydl_opts = {
            'quiet': True,
            'skip_download': True,
            'format': 'bestaudio/best' if solo_audio else 'best',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            download_url = info['url']
            title = info.get('title', 'video')

            filename = f"{title}.mp3" if solo_audio else f"{title}.mp4"

        return jsonify({
            "filename": filename,
            "download_url": download_url
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/tt-download', methods=['POST'])
def download_tiktok():
    data = request.json
    url = data.get("url")

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        ydl_opts = {
            'quiet': True,
            'skip_download': True,
            'forceurl': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            download_url = info['url']
            filename = info.get('title', 'video_tiktok.mp4')

        return jsonify({
            "filename": filename,
            "download_url": download_url
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/fb-download', methods=['POST'])
def download_facebook():
    data = request.json
    url = data.get("url")

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        ydl_opts = {
            'quiet': True,
            'skip_download': True,
            'forceurl': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            download_url = info['url']
            filename = info.get('title', 'video_facebook.mp4')

        return jsonify({
            "filename": filename,
            "download_url": download_url
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/ig-download', methods=['POST'])
def download_instagram():
    data = request.json
    url = data.get("url")

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        ydl_opts = {
            'quiet': True,
            'skip_download': True,
            'forceurl': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            download_url = info['url']
            title = info.get('title', 'instagram_video.mp4')

        return jsonify({
            "filename": title,
            "download_url": download_url
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
