import random
from locust import HttpUser, task, between

class StandardUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def index_page(self):
        self.client.get('/')

    @task(5)
    def meme_drake_hotline_bling(self):
        self.client.get('/meme/181913649', name='top3')

    @task(4)
    def meme_distracted_boyfriend(self):
        self.client.get('/meme/112126428', name='top3')

    @task(3)
    def meme_two_buttons(self):
        self.client.get('/meme/87743020', name='top3')

    @task(2)
    def meme_change_my_mind(self):
        self.client.get('/meme/129242436', name='other')

    @task(1)
    def meme_shut_up_and_take_my_money_fry(self):
        self.client.get('/meme/176908', name='other')
