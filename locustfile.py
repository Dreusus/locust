from locust import HttpUser, task, between

from config import config


class WebsiteUser(HttpUser):
    host = config['host']
    wait_time = between(config.get('min_wait'), config.get('max_wait'))

    def safe_request(self, url, name=None, **kwargs):
        try:
            return self.client.get(url, name=name, **kwargs)
        except Exception as e:
            print(f"Ошибка при выполнении запроса на {url}: {e}")

    @task
    def click_classic(self):
        self.safe_request("/click/333/777", name='Классик клик')

    @task
    def click_tb(self):
        self.safe_request("/click/333/555", name='Переход на ТБ')

    @task
    def click_default_tb(self):
        self.safe_request("/click/1/830", name='Переход на дефолт ТБ')

    @task
    def click_chain_tb(self):
        self.safe_request("/click/222/777", name='Цепочка ТБ')
