import React, { useState } from 'react';
import './Button.css'
import './PlayButton.css';

function PlayButton() {

  const [liked, setLiked] = useState(false);

  const handleToggle = () => {
    setLiked((prevValue) => !prevValue);
  };

  const playPlaylist = async () => {
    try {
      if (liked) {
        playLikedPlaylist();
      } else {
        // Call playPlaylist function
        const response = await fetch('http://localhost:5000/playlist');
        // Handle the response as needed
      }
    } catch (error) {
      // Handle any errors
    }
  };


 const playPlaylistShuffled = async () => {
    try {
      if (liked) {
        playLikedPlaylistShuffled();
      } else {
        // Call playPlaylist function
        const response = await fetch('http://localhost:5000/playlistshuffle');
        // Handle the response as needed
      }
    } catch (error) {
      // Handle any errors
    }
  };

 const playLikedPlaylistShuffled = async () => {
    try {
      const response = await fetch('http://localhost:5000/likedplaylistshuffle');
      // Handle the response as needed
    } catch (error) {
        // Handle any errors
    }
  };

 const playLikedPlaylist = async () => {
    try {
      const response = await fetch('http://localhost:5000/likedplaylist');
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

  const endPlayer = async () => {
    try {
      const response = await fetch('http://localhost:5000/player', {
        method: 'POST',
        mode: 'cors',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ choice: 'e' }),
      });
      // Handle the response as needed
    } catch (error) {
      // Handle any errors
    }
  };

  return (
    <div>
      <div>
        <label htmlFor="toggle">Liked songs only? </label>
        <input
        type="checkbox"
        id="toggle"
        checked={liked === true}
        onChange={handleToggle}
        />
        <button onClick={playPlaylist} className="button">Play playlist</button>
        <button onClick={playPlaylistShuffled} className="button">Shuffle Play</button>
      </div>
      <div>
        <button onClick={endPlayer} className="end-button">
        </button>
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
