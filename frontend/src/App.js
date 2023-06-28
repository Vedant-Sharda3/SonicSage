import React, { useState, useEffect } from 'react';
import './App.css';
import PlayButton from './components/PlayButton';
import InputButton from './components/InputButton';

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

function App() {
  const [inputText, setInputText] = useState("");
  const [title, setTitle] = useState("");

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

    fetchTitle();
  }, [inputText]);

  return (
    <div className="App">
      <header className="SonicSage">
        <h1> This is SonicSage </h1>
      </header>
      <body className="App">
        <InputButton name={title} />
        <PlayButton />
        <input type="text" onChange={handleChange} value={inputText} class='inputbox'/>
        <p>Song Result: {title}</p>
      </body>
    </div>
  );
}

export default App;
