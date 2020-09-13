import fetch from 'isomorphic-unfetch'
import Container from 'react-bootstrap/Container'

import Layout from '../components/layout'
import Meme from '../components/meme'
import { shuffle } from '../helpers/array'

const Index = ({ memes }) => {
    return (
        <Layout>
            <div>
                <h1>Welcome to my Awesome Web App</h1>
                <h3>Memes List</h3>
                <Container fluid>
                    {shuffle(memes).map((meme) => {
                        return <Meme key={meme.id} meme={meme} />
                    })}
                </Container>
            </div>
        </Layout>
    )
}

Index.getInitialProps = async function () {
    const response = await fetch(`https://api.imgflip.com/get_memes`)
    const result = await response.json()
    return { memes: result.data.memes }
}

export default Index
