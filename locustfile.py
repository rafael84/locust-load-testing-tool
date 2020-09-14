import random
from locust import task, between
from common.webdriver import WebdriverUser

class BrowserUser(WebdriverUser):
    wait_time = between(2, 5)

    meme_ids = None

    @task
    def index_page(self):
        self.client.go('/')

    @task(5)
    def meme_page(self):
        if self.meme_ids is None:
            return
        meme_id = random.choice(self.meme_ids)
        self.client.go('/meme/{}'.format(meme_id))

    def on_start(self):
        #
        # load meme_ids from initial page
        #
        self.client.go('/')
        cards = self.client.parse().find_all('div', class_='meme-card')
        self.meme_ids = [card.attrs['memeid'] for card in cards]
