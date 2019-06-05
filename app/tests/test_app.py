import sys
sys.path.append('../')
sys.path.append('../../')

from main import app
from unittest import TestCase, main

class TestApp(TestCase):

    def setUp(self):
        self.test_app = app.test_client()
        
    def test_get_index(self):
        response = self.test_app.get('/')
        self.assertEqual(200, response.status_code)

    def test_db_connection(self):
        response = self.test_app.get('/rank/anything')
        self.assertEqual(200, response.status_code, 'Database not found')


if __name__ == '__main__':
    main()