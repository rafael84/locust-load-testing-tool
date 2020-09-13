import Link from 'next/link'

const Meme = ({ meme }) => {
    return (
        <div className="meme-card" memeId={meme.id}>
            <Link href="/meme/[id]" as={`/meme/${meme.id}`}>
                <div>
                    <img src={meme.url} width={180} alt={meme.name} />
                    <p>{meme.name}</p>
                </div>
            </Link>
            <style jsx>{`
                div.meme-card {
                    cursor: pointer;
                    background: rgba(0, 0, 0, 0.3);
                    border-radius: 8px;
                    width: 200px;
                    display: inline-block;
                    border: 1px solid #333;
                    padding: 0.75rem;
                    margin: 0.5rem;
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
