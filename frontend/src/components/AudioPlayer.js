import React, { useRef } from 'react'


class AudioPlayer extends React.Component {

  render() {
    return (
      <div>
        <audio ref={useRef<HTMLAudioElement>(null)} src={"/Roar.mp3"} >
        Your browser doesnt support the audio element
        </audio>
      </div>
    );
  }
}

export default AudioPlayer;