import React, { useState, useEffect } from 'react';
import './App.css';
import PlayButton from './components/PlayButton';
import InputButton from './components/InputButton';

function App() {
  return (
    <div className="App">
      <header className="SonicSage">
        <InputButton />
        <PlayButton />
      </header>
    </div>
  )
}

export default App;
