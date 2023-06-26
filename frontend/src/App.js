import React, { useState, useEffect } from 'react';
import './App.css';
import PlayButton from './components/PlayButton';
//import InputButton from './components/InputButton';

function posty() {
    fetch("http://localhost:5000/play", {
                    method: 'POST', mode: 'cors', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({"song": "Metro Boomin"})
                })

}


function InputButton() {
    //const
    return (
    <button onClick={posty}>
        Play Metro
    </button>
    )
}

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
