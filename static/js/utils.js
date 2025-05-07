var card = {
    youtube: function() {
        const pre = document.getElementById("yt-card-body-pre");
        const pos = document.getElementById("yt-card-body-post");
        const fb = document.getElementById("fb-card");
        const tt = document.getElementById("tt-card");
        const ig = document.getElementById("ig-card");

        if (pre.style.display === "block") {
            pre.style.display = "none";
            pos.style.display = "block";
            fb.style.display = "none";
            tt.style.display = "none";
            ig.style.display = "none";
        };
    },
    facebook: function() {
        const pre = document.getElementById("fb-card-body-pre");
        const pos = document.getElementById("fb-card-body-post");
        const yt = document.getElementById("yt-card");
        const tt = document.getElementById("tt-card");
        const ig = document.getElementById("ig-card");

        if (pre.style.display === "block") {
            pre.style.display = "none";
            pos.style.display = "block";
            yt.style.display = "none";
            tt.style.display = "none";
            ig.style.display = "none";
        };
    },
    tiktok: function() {
        const pre = document.getElementById("tt-card-body-pre");
        const pos = document.getElementById("tt-card-body-post");
        const yt = document.getElementById("yt-card");
        const fb = document.getElementById("fb-card");
        const ig = document.getElementById("ig-card");

        if (pre.style.display === "block") {
            pre.style.display = "none";
            pos.style.display = "block";
            yt.style.display = "none";
            fb.style.display = "none";
            ig.style.display = "none";
        };
    },
    instagram: function() {
        const pre = document.getElementById("ig-card-body-pre");
        const pos = document.getElementById("ig-card-body-post");
        const yt = document.getElementById("yt-card");
        const fb = document.getElementById("fb-card");
        const tt = document.getElementById("tt-card");

        if (pre.style.display === "block") {
            pre.style.display = "none";
            pos.style.display = "block";
            yt.style.display = "none";
            fb.style.display = "none";
            tt.style.display = "none";
        };
    }
};
var reload = function() {
    location.reload();
}