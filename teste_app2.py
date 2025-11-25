import unittest
from app import app
import json

class AdvancedAPITests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    # 1) Teste de método HTTP inválido (robustez)
    def test_invalid_method_on_items(self):
        response = self.client.post('/items')
        self.assertEqual(response.status_code, 405)

    # 2) Teste de estrutura do JSON (formato da resposta)
    def test_items_json_structure(self):
        response = self.client.get('/items')
        data = json.loads(response.data)

        self.assertIsInstance(data, dict)
        self.assertIn('items', data)
        self.assertIsInstance(data['items'], list)

    # 3) Teste de tempo de resposta (performance básica)
    def test_response_time(self):
        import time
        start = time.time()
        response = self.client.get('/')
        end = time.time()

        self.assertEqual(response.status_code, 200)
        self.assertLess(end - start, 1)  # menos de 1 segundo

if __name__ == "__main__":
    unittest.main()