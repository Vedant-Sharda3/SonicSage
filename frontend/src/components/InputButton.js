function posty() {
    fetch("http://localhost:5000/play", {
                    method: 'POST', headers: { 'Referer': 'http://localhost:5000/', 'Content-Type': 'application/json' }, body: JSON.stringify({"song": "Metro Boomin"})
                })

}

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

function InputButton() {
    //const
    return (
    <button onClick={posty}>
        Play Metro
    </button>
    )
}

export default InputButton;