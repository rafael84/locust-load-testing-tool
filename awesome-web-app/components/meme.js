const Meme = ({ meme }) => {
    return (
        <div>
            <img src={meme.url} width={180} alt={meme.name} />
            <p>{meme.name}</p>
            <style jsx>{`
                div {
                    width: 200px;
                    display: inline-block;
                    border: 1px solid #333;
                    padding: 1rem;
                }
                p {
                    margin-top: 1rem;
                    font-size: 1.2rem;
                    word-break: break-word;
                }
            `}</style>
        </div>
    )
}

export default Meme
