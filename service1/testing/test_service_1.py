from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_page(self):
        with patch("requests.get") as g:
            with patch("requests.get") as v:
                with patch("requests.post") as p:
                    g.return_value.text = "Midfield"
                    v.return_value.text = "Arsenal"
                    p.return_value.text = "Mesut Ozil"

                    response = self.client.get(url_for('index'))
                    self.assertIn(b'Your player is Mesut Ozil, they play in the Midfield position for Arsenal')
