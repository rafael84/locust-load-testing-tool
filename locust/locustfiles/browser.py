"""
Uses Selenium Webdriver (Chrome) as a client.

For educational purposes only. Not advised to mix performance and functional tests:
https://www.selenium.dev/documentation/en/worst_practices/performance_testing/
"""

import os
import time
import random
from locust import User, task, between
from selenium import webdriver
from bs4 import BeautifulSoup

class WebdriverClient:
    _locust_environment = None
    webdriver = None

    def __init__(self, environment):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        webdriver_server = os.environ.get('WEBDRIVER_SERVER')
        self._locust_environment = environment
        self.webdriver = webdriver.Remote(command_executor=webdriver_server, options=options)

    def __del__(self):
        self.webdriver.quit()

    def go(self, path, name=None):
        """
        Loads a web page in the current browser session.
        """
        if name is None:
            name = path
        start_time = time.time()
        try:
            abs_path = '{}{}'.format(self._locust_environment.host, path)
            self.webdriver.get(abs_path)
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            self._locust_environment.events.request_failure.fire(
                request_type="webdriver",
                name=name,
                response_time=total_time,
                exception=e,
                response_length=0
            )
        else:
            total_time = int((time.time() - start_time) * 1000)
            self._locust_environment.events.request_success.fire(
                request_type="webdriver",
                name=name,
                response_time=total_time,
                response_length=0
            )

    def parse(self):
        page_html = self.webdriver.page_source
        return BeautifulSoup(page_html, 'html.parser')


class WebdriverUser(User):
    """
    This is the abstract User class which should be subclassed. It provides webdriver client
    that can be used to make requests through a web browser that will be tracked in Locust's statistics.
    """

    abstract = True

    def __init__(self, *args, **kwargs):
        super(WebdriverUser, self).__init__(*args, **kwargs)
        self.client = WebdriverClient(self.environment)

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
        self.client.go('/meme/{}'.format(meme_id), name='/meme/[id]')

    def on_start(self):
        #
        # load meme_ids from initial page
        #
        self.client.go('/')
        cards = self.client.parse().find_all('div', class_='meme-card')
        self.meme_ids = [card.attrs['memeid'] for card in cards]
