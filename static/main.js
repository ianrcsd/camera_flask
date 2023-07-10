var videoElement = document.getElementById('video');
var stream = null;

function startCamera() {
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(function(stream) {
                videoElement.srcObject = stream;
                videoElement.play();
            })
            .catch(function(error) {
                console.log('Error accessing camera:', error);
            });
    } else {
        console.log('getUserMedia is not supported');
    }
}

function stopCamera() {
    if (stream) {
        var tracks = stream.getTracks();
        tracks.forEach(function(track) {
            track.stop();
        });
        videoElement.srcObject = null;
    }
}
