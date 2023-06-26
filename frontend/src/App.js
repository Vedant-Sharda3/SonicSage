import React, {useState, useEffect } from 'react';
//import './App.css';
import PlayButton from './components/PlayButton';
import AudioPlayer from './components/AudioPlayer';
function App() {


  return (
    <div className="App">
      <header className="SonicSage">
        <AudioPlayer />
      </header>
    </div>
  );
}

export default App;
