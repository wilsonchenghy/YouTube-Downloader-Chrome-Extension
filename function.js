document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('downloadVideoButton').addEventListener('click', function() {
        GETRequestToDownloadVideo()
    })
})

function GETRequestToDownloadVideo () {
    let youTubeUrl = document.getElementById('youTubeUrl').value;

    fetch(`http://127.0.0.1:8000/downloadVideo?youTubeUrl=${youTubeUrl}`)
        .catch(error => console.log(error))
}



document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('downloadPlaylistButton').addEventListener('click', function() {
        GETRequestToDownloadPlaylist()
    })
})

function GETRequestToDownloadPlaylist () {
    let playlistUrl = document.getElementById('playlistUrl').value;

    fetch(`http://127.0.0.1:8000/downloadPlaylist?playlistUrl=${playlistUrl}`)
        .catch(error => console.log(error))
}