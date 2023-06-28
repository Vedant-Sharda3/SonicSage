import React from 'react';
import './Button.css'
import './PlayButton.css';

function PlayButton() {
  const playPlaylist = async () => {
    try {
      const response = await fetch('http://localhost:5000/playlist');
      // Handle the response as needed
    } catch (error) {
      // Handle any errors
    }
  };

  const pausePlayer = async () => {
    try {
      const response = await fetch('http://localhost:5000/player', {
        method: 'POST',
        mode: 'cors',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ choice: 'p' }),
      });
      // Handle the response as needed
    } catch (error) {
      // Handle any errors
    }
  };

  const resumePlayer = async () => {
    try {
      const response = await fetch('http://localhost:5000/player', {
        method: 'POST',
        mode: 'cors',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ choice: 'r' }),
      });
      // Handle the response as needed
    } catch (error) {
      // Handle any errors
    }
  };

  const nextPlayer = async () => {
    try {
      const response = await fetch('http://localhost:5000/player', {
        method: 'POST',
        mode: 'cors',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ choice: 'n' }),
      });
      // Handle the response as needed
    } catch (error) {
      // Handle any errors
    }
  };

  return (
    <div>
      <div>
        <button onClick={playPlaylist} className="button">Play playlist</button>
      </div>
      <div>
        <button onClick={pausePlayer} className="pause-button">
        </button>
        <button onClick={resumePlayer} className="resume-button">
        </button>
        <button onClick={nextPlayer} className="next-button">
        </button>
      </div>
    </div>
  );
}

export default PlayButton;
