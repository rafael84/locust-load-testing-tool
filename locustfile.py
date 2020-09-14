import os
from locust import HttpUser, task, between
from selenium import webdriver

def new_chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    webdriver_server = os.environ.get('WEBDRIVER_SERVER')
    return webdriver.Remote(command_executor=webdriver_server, options=options)

def host_path(client, path):
    return '{}/{}'.format(client.environment.host, path)

class Alice(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        self.webdriver = new_chrome_driver()

    @task
    def index_page(self):
        self.client.get(host_path(self, "/"))

    @task
    def meme_page(self):
        pass

    def on_stop(self):
        self.webdriver.quit()
