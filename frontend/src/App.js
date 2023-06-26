import React from 'react';
import './App.css';

function MyButton() {
    return (
    <button>
        Play Iris
    </button>
    );
}

const fetchData = () => {
fetch('http://localhost:5000/plays')
  .then(response => response.json())
  .catch(error => console.error('Error:', error));
};

function App() {
  return (
    <div className="App">
      <header className="SonicSage">

        <MyButton onClick={fetchData} />
      </header>
    </div>
  );
}

export default App;
