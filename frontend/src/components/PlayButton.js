function PlayButton() {
    return (
    <button onClick={()=>fetch("http://localhost:5000/playlist")}>
        Play dumbo
    </button>
    )
}

export default PlayButton;