from locust import HttpUser, task, constant, SequentialTaskSet


class MyScript(SequentialTaskSet):
    @task
    def get_xml(self):
        result = self.client.get("/xml", name="XML")
        print(result)

    @task
    def get_json(self):
        expected_response = "Wake up WonderWidgets!"

        with self.client.get("/json", catch_response=True, name="JSON") as response:
            result = True if expected_response in response.text else False
            print(self.get_json.__name__, result)
            response.success()
