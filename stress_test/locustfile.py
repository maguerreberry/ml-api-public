import time
from locust import HttpUser, task

class QuickstartUser(HttpUser):

    @task(1)
    def index(self):
        self.client.get('/')

    @task(2)
    def predict(self):
        self.client.post('/predict', params={'text':'bad'})
        self.client.post('/predict', params={'text':'good'})

    @task(3)
    def fail(self):
        self.client.post('/predict', params={})

    def on_start(self):
        pass
