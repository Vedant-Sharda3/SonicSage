import React from 'react';
import './Microphone.css'; // Import the CSS file
import microphone from './images/microphone.png';

const MicrophoneButton = () => {
  const callFlaskAPI = async () => {
    try {
      // Make a POST request to the Flask API endpoint
      const response = await fetch('http://localhost:5000/micro');

      // Handle the response from the API
      if (response.ok) {
        // API request was successful
        const data = await response.json();
        console.log('API response:', data);
      } else {
        // API request failed
        console.log('API request failed:', response.statusText);
      }
    } catch (error) {
      console.error('Error calling Flask API:', error);
    }
  };

  return (
    <div>
      <button onClick={callFlaskAPI}><img src={microphone} alt="Microphone" class="microphone-icon"/></button>
    </div>
  );
};

export default MicrophoneButton;
