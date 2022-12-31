from locust import TaskSet, constant, task, HttpUser, User
import random


class MyHttpCat(TaskSet):

    @task
    def get_status(self):
        self.client.get("/200")
        print("Get status of 200")
        self.interrupt(reschedule=False)

    @task
    def get_random_status(self):
        status_codes = [100, 101, 102, 202, 410, 510]
        random_url = "/" + str(random.choice(status_codes))
        response = self.client.get(random_url)
        print("Random http status")
        self.interrupt(reschedule=False)


class MyAnotherHTTPCat(TaskSet):

    @task
    def get_500_status(self):
        self.client.get("/500")
        print("Get status of 500")
        self.interrupt(reschedule=False)


class MyLoadTest(HttpUser):
    host = "https://http.cat"
    wait_time = constant(1)
    tasks = [MyHttpCat, MyAnotherHTTPCat]
