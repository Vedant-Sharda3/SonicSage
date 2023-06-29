function downloadIt(name) {
    fetch("http://localhost:5000/play", {
                    method: 'POST', mode: 'cors', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({"song": name})
                })
}


function searchBtn(input) {
    //const
    return (
    <button onClick={() => getTitle(input)}>
        Search
    </button>
    )
}


export default InputButton;