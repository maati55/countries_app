import unittest
import requests

class SimplisticTest(unittest.TestCase):
    def test(self):
        self.assertTrue(True)
    
class TestCase(unittest.TestCase):
    def test_index(self):
        r = requests.get("http://0.0.0.0:8080/")
        self.assertEqual(r.status_code, 200)

    def test_person_endpoint(self):
        r = requests.get('http://0.0.0.0:8080/healthcheck')
        self.assertEqual(r.status_code, 200)
        json_dict = r.json()
        self.assertEqual(json_dict['status'], 'success')

if __name__ == '__main__':
    unittest.main()
