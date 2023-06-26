import React, { useState, useEffect } from 'react';
import './App.css';
import PlayButton from './components/PlayButton';
import InputButton from './components/InputButton';



function App() {
  const [inputText, setInputText] = useState("");
  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    setInputText(e.target.value);
  };
  return (
    <div className="App">
      <header className="SonicSage">
        <InputButton />
        <PlayButton />
      </header>
      <body className="App">
        <input type="text" onChange={handleChange} value={inputText} />
        <p>Resultant: {inputText}</p>
      </body>
    </div>
  )
}

export default App;
