import { useState, useEffect } from 'react'
import { useRouter } from 'next/router'
import Link from 'next/link'
import fetch from 'isomorphic-unfetch'
import Button from 'react-bootstrap/Button'
import Container from 'react-bootstrap/Container'

import Layout from '../../components/layout'

const Meme = ({ memes }) => {
    const router = useRouter()
    const { id } = router.query

    const [meme, setMeme] = useState(null)

    useEffect(() => {
        const meme = memes.find((meme) => meme.id == id)
        setMeme(meme)
    })

    if (meme == null) {
        return null
    }

    return (
        <Layout>
            <Container fluid>
                <div>
                    <h1>{meme.name}</h1>
                    <div className="buttons">
                        <Link href="/">
                            <Button className="back-button" variant="primary">
                                Back
                            </Button>
                        </Link>
                        <Button
                            className="check-versions-link"
                            href={`https://imgflip.com/meme/${meme.id}`}
                            target="_blank"
                            variant="link">
                            Check versions in imgflip
                        </Button>
                        <Button
                            className="create-my-version-link"
                            href={`https://imgflip.com/memegenerator/${meme.id}`}
                            target="_blank"
                            variant="link">
                            Create my version
                        </Button>
                    </div>
                    <img src={meme.url} />
                </div>
            </Container>
            <style jsx>{`
                img {
                    margin: 1rem auto;
                    max-width: 100vh;
                }
            `}</style>
        </Layout>
    )
}

export async function getStaticProps() {
    const response = await fetch(`https://api.imgflip.com/get_memes`)
    const result = await response.json()
    return { props: { memes: result.data.memes } }
}

export async function getStaticPaths() {
    const response = await fetch(`https://api.imgflip.com/get_memes`)
    const result = await response.json()
    const paths = result.data.memes.map((meme) => ({ params: { id: meme.id } }))
    return {
        paths,
        fallback: false
    }
}

export default Meme
