function PlayButton() {
    return (
    <button onClick={()=>{
        console.log("Hello")
        fetch("http://localhost:5000/plays").then(
            response => response.json()
        ).then(
            data => {
                console.log(data)
            }
        )
        }}>
        Plays Roar
    </button>
    );
}

export default PlayButton;