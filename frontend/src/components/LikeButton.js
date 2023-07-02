import './Button.css'

function like() {
    const response = fetch("http://localhost:5000/like")
    console.log(response)
}

function LikeButton() {
    //const
    return (
    <button onClick={() => like()} class='button'>
        ❤️
    </button>
    )
}


export default LikeButton;