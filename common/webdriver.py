import os
import time
from locust import User, events
from selenium import webdriver
from bs4 import BeautifulSoup

class WebdriverClient:
    """
    Uses Selenium Webdriver (Chrome) as a client.

    For educational purposes only. Not advised to mix performance and functional tests:
    https://www.selenium.dev/documentation/en/worst_practices/performance_testing/
    """
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

    # def on_stop(self):
    #     self.client.webdriver.quit()
