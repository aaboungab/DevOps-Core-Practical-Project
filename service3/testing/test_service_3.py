from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):

    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_arsenal_team(self):
        with patch('random.randrange') as r:
            r.return_value = 0
            response = self.client.get(url_for('team'))
            self.assertIn(b'Arsenal', response.data)

    def test_chelsea_team(self):
        with patch('random.randrange') as r:
            r.return_value = 1
            response = self.client.get(url_for('team'))
            self.assertIn(b'Chelsea', response.data)

    def test_liverpool_team(self):
        with patch('random.randrange') as r:
            r.return_value = 2
            response = self.client.get(url_for('team'))
            self.assertIn(b'Liverpool', response.data)