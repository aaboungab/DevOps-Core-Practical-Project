from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):

    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_striker_position(self):
        with patch('random.randrange') as r:
            r.return_value = 0
            response = self.client.get(url_for('position'))
            self.assertIn(b'Striker', response.data)
    
    def test_midfield_position(self):
        with patch('random.randrange') as r:
            r.return_value = 1
            response = self.client.get(url_for('position'))
            self.assertIn(b'Midfield', response.data)
    
    def test_centerback_position(self):
        with patch('random.randrange') as r:
            r.return_value = 2
            response = self.client.get(url_for('position'))
            self.assertIn(b'CenterBack', response.data)