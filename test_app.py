
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flaskr import create_app
from models import setup_db, Actors, Movies


class CapstoneTestCase(unittest.TestCase):
    """This class represents the capstone project test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgres://txdjjhlbnduuhp:2d1346031b" +\
            "75afc27357c0cba50053231c6cb1c81606f27b0c64dc30d93702ce" +\
            "@ec2-52-202-66-191.compute-1.amazonaws.com:5432/dbhh4ikpsi78ag"
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.movie = {
            "title": "Tenet",
            "release_date": "2020-8-27"
        }

        self.actor = {
            "name": "Michael Cain",
            "age": 65,
            "gender": 'M',
        }

        # Set up authentication tokens info
        with open('auth_config.json', 'r') as f:
            self.auth = json.loads(f.read())

        assistant_jwt = self.auth["roles"]["Casting Assistant"]["jwt_token"]
        director_jwt = self.auth["roles"]["Casting Director"]["jwt_token"]
        producer_jwt = self.auth["roles"]["Executive Producer"]["jwt_token"]
        bad_jwt = self.auth["roles"]["No Role"]["jwt_token"]
        self.auth_headers = {
            "Casting Assistant": f'Bearer {assistant_jwt}',
            "Casting Director": f'Bearer {director_jwt}',
            "Executive Producer": f'Bearer {producer_jwt}',
            "No Role": f'Bearer {bad_jwt}'
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

    # GET /movies - all movies
    def test_get_movies(self):
        auth_header = {
            "Authorization": self.auth_headers["Casting Assistant"]
        }
        res = self.client().get('/movies', headers=auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue(data['total_movies'])

    def test_get_movies_failed(self):
        auth_header = {
            "Authorization": self.auth_headers["Casting Assistant"]
        }
        res = self.client().get('/movies/', headers=auth_header)
        data = json.loads(res.data)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['success'], False)

    def test_get_movies_auth_failed(self):
        auth_header = {
            "Authorization": self.auth_headers["No Role"]
        }
        res = self.client().get('/movies?page=1000', headers=auth_header)
        data = json.loads(res.data)
        self.assertEqual(data['error'], 401)
        self.assertEqual(data['success'], False)

    # GET /actors - all actors
    def test_get_actors(self):
        auth_header = {
            "Authorization": self.auth_headers["Casting Assistant"]
        }
        res = self.client().get('/actors', headers=auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
        self.assertTrue(data['total_actors'])

    def test_get_actors_failed(self):
        auth_header = {
            "Authorization": self.auth_headers["Casting Assistant"]
        }
        res = self.client().get('/actors/', headers=auth_header)
        data = json.loads(res.data)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['success'], False)

    # GET /actor
    def test_get_actor(self):
        auth_header = {
            "Authorization": self.auth_headers["Casting Assistant"]
        }
        res = self.client().get('/actors/1', headers=auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['name'])
        self.assertTrue(data['age'])
        self.assertTrue(data['gender'])

    def test_get_actor_failed(self):
        auth_header = {
            "Authorization": self.auth_headers["Casting Assistant"]
        }
        res = self.client().get('/actors/999', headers=auth_header)
        data = json.loads(res.data)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['success'], False)

    # GET /movie
    def test_get_movie(self):
        auth_header = {
            "Authorization": self.auth_headers["Casting Assistant"]
        }
        res = self.client().get('/movies/1', headers=auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['title'])
        self.assertTrue(data['release_date'])

    def test_get_movie_failed(self):
        auth_header = {
            "Authorization": self.auth_headers["Casting Assistant"]
        }
        res = self.client().get('/movies/999', headers=auth_header)
        data = json.loads(res.data)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['success'], False)

    # DELETE /movie
    def delete_movie(self):
        auth_header = {
            "Authorization": self.auth_headers["Executive Producer"]
        }
        res = self.client.delete('/movies/1', headers=auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def delete_movie_failed(self):
        auth_header = {
            "Authorization": self.auth_headers["Executive Producer"]
        }
        res = self.client.delete('/movies/12341', headers=auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)

    def delete_movie_auth_failed(self):
        auth_header = {
            "Authorization": self.auth_headers["asdf"]
        }
        res = self.client.delete('/movies/12341', headers=auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)

    # DELETE /actor
    def delete_actor(self):
        auth_header = {
            "Authorization": self.auth_headers["Casting Director"]
        }
        res = self.client.delete('/actors/1', headers=auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def delete_actor_failed(self):
        auth_header = {
            "Authorization": self.auth_headers["Casting Director"]
        }
        res = self.client.delete('/actors/12341', headers=auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)

    def delete_actor_auth_failed(self):
        auth_header = {
            "Authorization": self.auth_headers["asadf"]
        }
        res = self.client.delete('/actors/12341', headers=auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)

    # POST /actor
    def post_actor(self):
        auth_header = {
            "Authorization": self.auth_headers["Casting Director"]
        }
        res = self.client.post(
            '/actors',
            json={
                'name': 'Samuel L Jackson',
                'age': 66,
                'gender': 'Male'},
            headers=auth_header)
        data = json.loads(res.data)
        self.assertTrue(data['success'])
        self.assertEqual(res.status_code, 200)

    def post_actor_failed(self):
        auth_header = {
            "Authorization": self.auth_headers["Casting Director"]
        }
        res = self.client.post(
            '/actors',
            json={
                'name': True,
                'age': 66,
                'gender': 'Male'},
            headers=auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])

    # POST /movie
    def post_movie(self):
        auth_header = {
            "Authorization": self.auth_headers["Executive Producer"]
        }
        res = self.client.post(
            '/movies',
            json={
                'title': 'Silance of the Lambs',
                'release_date': '1991'},
            headers=auth_header)
        data = json.loads(res.data)
        self.assertTrue(data['success'])
        self.assertEqual(res.status_code, 200)

    def post_movie_failed(self):
        auth_header = {
            "Authorization": self.auth_headers["Executive Producer"]
        }
        res = self.client.post(
            '/movies',
            json={
                'title': True,
                'release_date': 1991},
            headers=auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])

    # PATCH /movie
    def edit_movie(self):
        auth_header = {
            "Authorization": self.auth_headers["Casting Director"]
        }
        res = self.client.patch(
            'movies/1',
            json={
                'title': 'The Departed',
                'release_date': '2006'},
            headers=auth_header)
        data = json.loads(res.data)
        self.assertTrue(data['success'])
        self.assertEqual(res.status_code, 200)

    def edit_movie_failed(self):
        res = self.client.patch(
            'movies/1982',
            json={
                'title': ' Departed',
                'release_date': '2006'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    # PATH /actor
    def edit_actor(self):
        auth_header = {
            "Authorization": self.auth_headers["Casting Director"]
        }
        res = self.client.patch(
            'actors/1',
            json={
                'name': 'Leonardo Dicaprio',
                'age': '43',
                'gender': 'Male'},
            headers=auth_header)
        data = json.loads(res.data)
        self.assertTrue(data['success'])
        self.assertEqual(res.status_code, 200)

    def edit_actor_failed(self):
        res = self.client.patch(
            'actors/1982',
            json={
                'name': 'Leonardo Dicaprio',
                'age': '43',
                'gender': 'Male'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
