from locust import HttpUser, task, between

from config import config


class WebsiteUser(HttpUser):
    host = config['host']
    wait_time = between(0, 0)

    @task
    def click_classic(self):
        self.client.get("/click/333/777", name='Классик клик')

    @task
    def click_tb(self):
        self.client.get("/click/333/555", name='Переход на ТБ')

    @task
    def click_default_tb(self):
        self.client.get("/click/1/830", name='Переход на дефолт ТБ')

    @task
    def click_chain_tb(self):
        self.client.get("/click/222/777", name='Цепочка ТБ')

    '''
    @task
    def click_innactive_offer_web(self):
        self.client.get("/click/272/762", name='дефолт веб дефолт оффер')
    '''
