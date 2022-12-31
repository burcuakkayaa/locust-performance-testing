import time

from locust import User, SequentialTaskSet, constant, HttpUser, task, constant_pacing


class MySeqTask(SequentialTaskSet):

    @task
    def get_status(self):
        self.client.get("/200")
        print("Get status of 200")

    @task
    def get_500_status(self):
        self.client.get("/500")
        print("Get status of 500")


class MyLoadTest(HttpUser):
    time.sleep(2)
    host = "https://http.cat"
    tasks = [MySeqTask]
