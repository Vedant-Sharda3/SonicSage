const name = 'Love'

function posty(name) {
    fetch("http://localhost:5000/play", {
                    method: 'POST', mode: 'cors', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({"song": name})
                })
}


function InputButton() {
    //const
    return (
    <button onClick={() => posty(name)}>
        Play Metro
    </button>
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