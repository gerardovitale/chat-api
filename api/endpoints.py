from api.app import app, api
from flask_restful import Resource, reqparse
from api.models import UserList, User, Publication

@app.route("/")
def hello_world():
    return {
        'result': 'Welcome to my API!',
        'status': 200
        }

api.add_resource(UserList, '/users/')
api.add_resource(User, '/users/<username>')
api.add_resource(Publication, '/publications')