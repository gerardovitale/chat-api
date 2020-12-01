from flask import Flask
from flask_restful import Resource, Api, reqparse

# creating a flask object
app = Flask(__name__)
api = Api(app)
