import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Movies, Actors
import json
import sys

from auth.auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type,Authorization,true')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,PUT,POST,DELETE,OPTIONS')
        return response

    # GET /actors

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:casting-assistant')
    def get_actors(payload):
        # make sure we can get all actors list
        actor_list = Actors.query.order_by(Actors.id).all()
        formatted_actors_list = [actor.format() for actor in actor_list]
        print(actor_list)
        return jsonify({
            'success': True,
            'actors': formatted_actors_list,
            'total_actors': len(formatted_actors_list)
        })

    # GET /movies
    @app.route('/movies', methods=['GET'])
    @requires_auth('get:casting-assistant')
    def get_movies(payload):
        # make sure we can get all actors list
        movie_list = Movies.query.order_by(Movies.id).all()
        formatted_movie_list = [movie.format() for movie in movie_list]
        return jsonify({
            'success': True,
            'movies': formatted_movie_list,
            'total_movies': len(formatted_movie_list)
        })

    # GET /actors/:actor_id

    @app.route('/actors/<int:actor_id>', methods=['GET'])
    @requires_auth('get:casting-assistant')
    def get_actors_by_id(payload, actor_id):
        # make sure we can get all actors list
        actor = Actors.query.filter(Actors.id == actor_id).one_or_none()
        if actor is None:
            abort(404)
        else:
            return jsonify({
                'success': True,
                'name': actor.name,
                'age': actor.age,
                'gender': actor.gender
            })

    # GET /movies/:movie_id

    @app.route('/movies/<int:movie_id>', methods=['GET'])
    @requires_auth('get:casting-assistant')
    def get_movie_by_id(payload, movie_id):
        movie = Movies.query.filter(Movies.id == movie_id).one_or_none()
        print(movie)
        if movie is None:
            abort(404)
        else:
            return jsonify({
                'success': True,
                'title': movie.title,
                'release_date': movie.release_date,
            })

    # DELETE /movies/:movie_id

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:executive-producer')
    def delete_movie_by_id(payload, movie_id):
        queued_movie = Movies.query.filter(Movies.id == movie_id).one_or_none()
        if queued_movie is None:
            abort(404)
        else:
            Movies.delete(queued_movie)
            return jsonify({
                "success": True,
                "delete": movie_id
            })

    # DELETE /actors/:actor_id

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:casting-director')
    def delete_actor_by_id(payload, actor_id):
        queued_actor = Actors.query.filter(Actors.id == actor_id).one_or_none()
        if queued_actor is None:
            abort(404)
        else:
            Actors.delete(queued_actor)
            return jsonify({
                "success": True,
                "delete": actor_id
            })

    # POST /movies

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:executive-producer')
    def add_movie(payload):
        error = False
        try:
            movie_to_add = Movies(title=request.json['title'],
                                  release_date=request.json['release_date'])
            Movies.insert(movie_to_add)
        except Exception:
            error = True
            print(sys.exc_info())
        finally:
            if error:
                abort(422)
            else:
                return jsonify({
                    'success': True,
                    'movie': [movie_to_add.format()]
                })

    # POST /actors

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:casting-director')
    def add_actor(payload):
        error = False
        try:
            actor_to_add = Actors(name=request.json['name'],
                                  age=request.json['age'],
                                  gender=request.json['gender'])
            Actors.insert(actor_to_add)
        except Exception:
            error = True
            print(sys.exc_info())
        finally:
            if error:
                abort(422)
            else:
                return jsonify({
                    'success': True,
                    'actor': [actor_to_add.format()]
                })

    # PATCH /actor/actor_id

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:casting-director')
    def edit_actor(payload, actor_id):
        queued_actor = Actors.query.filter(Actors.id == actor_id).one_or_none()

        if queued_actor is None:
            abort(404)
        else:
            if 'name' in request.json:
                queued_actor.name = request.json['name']
            if 'age' in request.json:
                queued_actor.age = request.json['age']
            if 'gender' in request.json:
                queued_actor.gender = request.json['gender']
            Actors.update(queued_actor)
            return jsonify({
                "success": True,
                "actor": [queued_actor.format()]
            })

    # PATCH /movie/movie_id

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:casting-director')
    def edit_movie(payload, movie_id):
        queued_movie = Movies.query.filter(Movies.id == movie_id).one_or_none()

        if queued_movie is None:
            abort(404)
        else:
            if 'title' in request.json:
                queued_movie.title = request.json['title']
            if 'release_date' in request.json:
                queued_movie.release_date = request.json['release_date']
            Movies.update(queued_movie)
            return jsonify({
                "success": True,
                "movie": [queued_movie.format()]
            })

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "internal server error"
        }), 500

    @app.errorhandler(AuthError)
    def authorization_error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error
        }), error.status_code

    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
