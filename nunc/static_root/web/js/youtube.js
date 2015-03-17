var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";

var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

var player;

function onYouTubeIframeAPIReady() {
  player = new YT.Player('player', {
    height: '200',
	width: '300',
	events: {
      'onStateChange': onPlayerStateChange
	  }
    });
}


function onReady(event) {
  event.target.playVideo();
}


// YT.PlayerState.ENDED
// YT.PlayerState.PLAYING
// YT.PlayerState.PAUSED
// YT.PlayerState.BUFFERING
// YT.PlayerState.CUED

function onPlayerStateChange(event) {
  if (event.data == YT.PlayerState.ENDED) {
    player.loadVideoById(playlist[index++ % playlist.length], 5, "large");
  }
}

function stopVideo() {
  player.stopVideo();
}
