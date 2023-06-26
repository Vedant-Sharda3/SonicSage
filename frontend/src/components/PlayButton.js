function PlayButton() {
    return (
    <button onClick={()=>fetch("http://localhost:5000/plays")}>
        Play dumbo
    </button>
    )
}

export default PlayButton;