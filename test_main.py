import unittest
from fastapi.testclient import TestClient
from main import app

class TestServer(unittest.TestCase):
    def test_root_path(self):
        client = TestClient(app)
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello CRC2025!"}

    def test_other_paths(self):
        client = TestClient(app)
        response = client.get("/nonexistent")
        assert response.status_code == 404

if __name__ == '__main__':
    unittest.main()
