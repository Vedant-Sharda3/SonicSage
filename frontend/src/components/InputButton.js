import './InputButton.css';
import './Button.css'

function posty(name) {
    const response = fetch("http://localhost:5000/play", {
        method: 'POST', mode: 'cors', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({"song": name['name']})
    })
    console.log(response)
}

function del(name) {
    const response = fetch("http://localhost:5000/delete", {
        method: 'POST', mode: 'cors', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({"song": name['name']})
    })
    console.log(response)
}

function queue(name) {
    const response = fetch("http://localhost:5000/queue", {
        method: 'POST', mode: 'cors', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({"song": name['name']})
    })
    console.log(response)
}

function InputButton(name) {
    //const
    return (
    <div>
    <button onClick={() => queue(name)} class='button'>
        Queue Song
    </button>
    <button onClick={() => posty(name)} class='button'>
        Play Song
    </button>
    <button onClick={() => del(name)} class='button'>
        Delete Song
    </button>
    </div>
    )
}


export default InputButton;

const Do_input = async (e) => {
    e.preventDefault();
    const response = await fetch('http://localhost:5000/play', {
      method: 'POST',
      body: JSON.stringify({"song": "Metro Boomin"}),
      headers: {
        'Content-Type': 'application/json'
      }
    });
    const result = await response.json();
    console.log(result);
  }