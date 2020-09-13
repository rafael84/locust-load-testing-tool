import Container from 'react-bootstrap/Container'

import Head from 'next/head'

const Layout = (props) => {
    return (
        <Container fluid>
            <Head>
                <title>Awesome Web App</title>
            </Head>

            <div>{props.children}</div>
        </Container>
    )
}

export default Layout
