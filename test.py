import unittest
import requests

class TestAPI(unittest.TestCase):

    URL = "http://127.0.0.1:5000/"

    def response(self):
        response = requests.get(self.URL)
        self.assertEqual(response.status_code,200)

if __name__=="__main__":
    tester = TestAPI()
    tester.response()
    