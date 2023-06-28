function PlayButton() {
    return (
    <button onClick={()=>fetch("http://localhost:5000/playlist")}>
        Play playlist
    </button>
    <div>
        <button onClick={()=>fetch("http://localhost:5000/player", {
        method: 'POST', mode: 'cors', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({"choice": 'p'})}>
            Pause
        </button>
    </div>
    )
}

export default PlayButton;