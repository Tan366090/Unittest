from ..APP import app  # Make sure this is the correct import path
import unittest

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_login_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Đăng nhập thành viên', response.get_data(as_text=True))

    def test_login_success(self):
        response = self.app.post('/', data=dict(
            email='user1',
            password='password1',
            ma_so='12345'
        ))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers['Location'], 'http://localhost/upload')  # Assuming the default server address

    def test_login_failure(self):
        response = self.app.post('/', data=dict(
            email='user1',
            password='wrongpassword',
            ma_so='12345'
        ))
        self.assertEqual(response.status_code, 404)
        self.assertIn('Invalid credentials!', response.get_data(as_text=True))

    # Add more test cases here

if __name__ == '__main__':
    unittest.main()