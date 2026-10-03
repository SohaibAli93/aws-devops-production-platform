import unittest
from app import app


class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_health_endpoint(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json(),
            {"status": "healthy"}
        )

    def test_home_endpoint(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)

        data = response.get_json()

        self.assertEqual(
            data["message"],
            "AWS DevOps Production Platform"
        )

        self.assertEqual(
            data["status"],
            "running"
        )

    def test_tasks_endpoint(self):
        response = self.client.get("/api/tasks")

        self.assertEqual(response.status_code, 200)

        data = response.get_json()

        self.assertEqual(len(data), 3)


if __name__ == "__main__":
    unittest.main()