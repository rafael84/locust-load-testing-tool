import time
from locust import HttpUser, task, between

class Alice(HttpUser):
    wait_time = between(1, 2)

    @task
    def index_page(self):
        self.client.get("/")

    @task
    def meme_page(self):
        pass
