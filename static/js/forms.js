var download = {
    youtube: async function(event) {
        event.preventDefault();

        const url = document.getElementById("yturl").value;
        const isAudio = document.getElementById("yttype").checked;
        const mensaje = document.getElementById("ytmensaje");
        const downloadBtn = document.getElementById("yt-download-btn");
        const downloadMsg = document.getElementById("yt-download-msg");
        

        mensaje.innerHTML = "⏳ Procesando...";
        downloadMsg.style.display = "block";

        try {
            const response = await fetch("../yt-download", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ url, isAudio })
            });

            const data = await response.json();
            if (!data.download_url) {
                mensaje.innerHTML = "❌ Error al obtener el enlace de descarga.";
                return;
            }

            if (downloadBtn.style.display = "none")
                {
                    downloadBtn.style.display = "block";
            };

            downloadBtn.href = data.download_url;
            downloadBtn.download = data.filename || "video.mp4";
            mensaje.innerHTML = "✅ Archivo Listo para descargar";
        }
        catch (error) {
            mensaje.innerHTML = "❌ Error Intentando descargar el Archivo, Intente nuevamente en unos instantes.";
        }
        

    },

    facebook: async function(event) {
        event.preventDefault();

        const url = document.getElementById("fburl").value;
        const mensaje = document.getElementById("fbmensaje");
        const downloadBtn = document.getElementById("fb-download-btn");
        const downloadMsg = document.getElementById("fb-download-msg");

        mensaje.innerHTML = "⏳ Procesando...";
        downloadMsg.style.display = "block";

        try {
            const response = await fetch("../fb-download", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ url})
            });

            const data = await response.json();
            if (!data.download_url) {
                mensaje.innerHTML = "❌ Error al obtener el enlace de descarga.";
                return;
            }

            if (downloadBtn.style.display = "none")
                {
                    downloadBtn.style.display = "block";
            };

            downloadBtn.href = data.download_url;
            downloadBtn.download = data.filename || "video.mp4";
            mensaje.innerHTML = "✅ Archivo Listo para descargar";
            
        }
        catch (error) {
            mensaje.innerHTML = "❌ Error Intentando descargar el Archivo, Intente nuevamente en unos instantes.";
        }
        

    },

    tiktok: async function(event) {
        event.preventDefault();

        const url = document.getElementById("tturl").value;
        const mensaje = document.getElementById("ttmensaje");
        const downloadBtn = document.getElementById("tt-download-btn");
        const downloadMsg = document.getElementById("tt-download-msg");

        mensaje.innerHTML = "⏳ Procesando...";
        downloadMsg.style.display = "block";

        try {
            const response = await fetch("../tt-download", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ url })
            });

            const data = await response.json();
            if (!data.download_url) {
                mensaje.innerHTML = "❌ Error al obtener el enlace de descarga.";
                return;
            }

            if (downloadBtn.style.display = "none")
                {
                    downloadBtn.style.display = "block";
            };

            downloadBtn.href = data.download_url;
            downloadBtn.download = data.filename || "video.mp4";
            mensaje.innerHTML = "✅ Archivo Listo para descargar";
            
        }
        catch (error) {
            mensaje.innerHTML = "❌ Error Intentando descargar el Archivo, Intente nuevamente en unos instantes.";
        }
        

    },

    instagram: async function(event) {
        event.preventDefault();

        const url = document.getElementById("igurl").value;
        const mensaje = document.getElementById("igmensaje");
        const downloadBtn = document.getElementById("ig-download-btn");
        const downloadMsg = document.getElementById("ig-download-msg");

        mensaje.innerHTML = "⏳ Procesando...";
        downloadMsg.style.display = "block";

        try {
            const response = await fetch("../ig-download", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ url})
            });

            const data = await response.json();
            if (!data.download_url) {
                mensaje.innerHTML = "❌ Error al obtener el enlace de descarga.";
                return;
            }

            if (downloadBtn.style.display = "none")
                {
                    downloadBtn.style.display = "block";
            };

            downloadBtn.href = data.download_url;
            downloadBtn.download = data.filename || "video.mp4";
            mensaje.innerHTML = "✅ Archivo Listo para descargar";
            
        }
        catch (error) {
            mensaje.innerHTML = "❌ Error Intentando descargar el Archivo, Intente nuevamente en unos instantes.";
        }
        

    }
}