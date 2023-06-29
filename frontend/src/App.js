import React, { useState, useEffect } from 'react';
import './App.css';
import PlayButton from './components/PlayButton';
import InputButton from './components/InputButton';
import TableDisplay from './components/TableDisplay';

async function getTitle(input) {
  if (input === '') {
        console.log('Empty')
        return '';
  }
  try {
    const response = await fetch("http://localhost:5000/title", {
      method: 'POST',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ "name": input })
    });

    if (response.ok) {
      const data = await response.json();
      const title = data.title;
      console.log(title);
      return title;
    } else {
      throw new Error('Request failed with status ' + response.status);
    }
  } catch (error) {
    console.error('Error:', error);
    throw error;
  }
}

async function getCurrent() {

  try {
    const response = await fetch("http://localhost:5000/current");

    if (response.ok) {
      const data = await response.json();
      const curr = data.current;
      return curr;
    } else {
      throw new Error('Request failed with status ' + response.status);
    }
  } catch (error) {
    console.error('Error:', error);
    throw error;
  }
}

function App() {
  const [inputText, setInputText] = useState("");
  const [title, setTitle] = useState("");
  const [currentSong, setCurrentSong] = useState("");

  const handleChange = (e) => {
    setInputText(e.target.value);
  };

  useEffect(() => {
    const fetchTitle = async () => {
      try {
        const fetchedTitle = await getTitle(inputText);
        setTitle(fetchedTitle);
      } catch (error) {
        // Handle the error as per your requirements
      }
    };
    const fetchCurrent = async () => {
      try {
        const fetchedCurrent = await getCurrent();
        setCurrentSong(fetchedCurrent);
      } catch (error) {
        // Handle the error as per your requirements
      }
    };
    const pollCurrent = () => {
      fetchCurrent();
      setTimeout(pollCurrent, 5000); // Polling interval: 5 seconds (adjust as needed)
    };

    fetchTitle();
    pollCurrent();
  }, [inputText]);

  return (
    <div className="App">
      <header className="SonicSage">
        <h1> ❤️ ------- SonicSage ------- ❤️ </h1>
        <h3> Currently Playing: {currentSong} </h3>
      </header>
      <body className="App">
        <InputButton name={title} />
        <PlayButton />
        <input type="text" onChange={handleChange} value={inputText} class='inputbox'/>
        <p>Song Result: {title}</p>
        <TableDisplay />
      </body>
    </div>
  );
}

export default App;
