from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):

    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_arsemal_st(self):
        with patch('requests.get') as i:
            i.return_value.text = 'Arsenal'
            with patch('random.randrange') as r:
                    r.return_value = 'Striker'
                    response = self.client.post(
                        url_for('name'),
                        data = 'Striker Arsenal')
                    self.assertIn(b'Pierre-Emerick Aubameyang', response.data)
    
    def test_arsenal_mid(self):
        with patch('requests.get') as i:
            i.return_value.text = 'Arsenal'
            with patch('random.randrange') as r:
                    r.return_value = 'Midfield'
                    response = self.client.post(
                        url_for('name'),
                        data = 'Midfield Arsenal')
                    self.assertIn(b'Mesut Ozil', response.data)
    
    def test_arsenal_cb(self):
        with patch('requests.get') as i:
            i.return_value.text = 'Arsenal'
            with patch('random.randrange') as r:
                    r.return_value = 'CenterBack'
                    response = self.client.post(
                        url_for('name'),
                        data = 'CenterBack Arsenal')
                    self.assertIn(b'Gabriel Magalhaes', response.data)
    
    def test_chelsea_st(self):
        with patch('requests.get') as i:
            i.return_value.text = 'Chelsea'
            with patch('random.randrange') as r:
                    r.return_value = 'Striker'
                    response = self.client.post(
                        url_for('name'),
                        data = 'Striker Chelsea')
                    self.assertIn(b'Olivier Giroud', response.data)
    
    def test_chelsea_mid(self):
        with patch('requests.get') as i:
            i.return_value.text = 'Chelsea'
            with patch('random.randrange') as r:
                    r.return_value = 'Midfield'
                    response = self.client.post(
                        url_for('name'),
                        data = 'Midfield Chelsea')
                    self.assertIn(b'Mateo Kovacic', response.data)
    
    def test_chelsea_cb(self):
        with patch('requests.get') as i:
            i.return_value.text = 'Chelsea'
            with patch('random.randrange') as r:
                    r.return_value = 'CenterBack'
                    response = self.client.post(
                        url_for('name'),
                        data = 'CenterBack Chelsea')
                    self.assertIn(b'Kurt Zouma', response.data)

    def test_liverpool_st(self):
        with patch('requests.get') as i:
            i.return_value.text = 'Liverpool'
            with patch('random.randrange') as r:
                    r.return_value = 'Striker'
                    response = self.client.post(
                        url_for('name'),
                        data = 'Striker Liverpool')
                    self.assertIn(b'Mohamed Salah', response.data)
    
    def test_liverpool_mid(self):
        with patch('requests.get') as i:
            i.return_value.text = 'Liverpool'
            with patch('random.randrange') as r:
                    r.return_value = 'Midfield'
                    response = self.client.post(
                        url_for('name'),
                        data = 'Midfield Liverpool')
                    self.assertIn(b'Georginio Wijnaldum', response.data)
    
    def test_liverpool_cb(self):
        with patch('requests.get') as i:
            i.return_value.text = 'Liverpool'
            with patch('random.randrange') as r:
                    r.return_value = 'CenterBack'
                    response = self.client.post(
                        url_for('name'),
                        data = 'CenterBack Liverpool')
                    self.assertIn(b'Virgil van Dijk', response.data)
