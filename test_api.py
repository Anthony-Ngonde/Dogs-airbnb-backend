import unittest
from app import create_app
from config import TestConfig
from exts import db


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app=create_app(TestConfig)

        self.client=self.app.test_client()

        with self.app.app_context():
            # db.init_app(self.app)

            db.create_all()
    
    def test_hello_world(self):
        hello_response = self.client.get('/hello')

        json = hello_response.get_json()

        # print(json)

        self.assertEqual(json,{"message":"Hello World"})

    
    def test_signup(self):
        signup_response = self.client.post('/signup',
            json = {"username":"testuser", "email":"testuser@test.com", "password":"password"}
        )

        status_code = signup_response.status_code

        # print(status_code)

        self.assertEqual(status_code, 201)

    


    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ ==  "__main__":
    unittest.main()
