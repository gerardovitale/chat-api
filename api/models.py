from flask_restful import Resource, reqparse
from helpers.mongo import get_data, insert_data, delete_data, update_publication, ObjectId
from bson.json_util import loads, dumps
from helpers.json_encoder import JSONEncoder

parser = reqparse.RequestParser()

class UserList(Resource):
    def get(self):
        return {
            'result': loads(JSONEncoder().encode(get_data('users'))),
            'status': 200
            }
    def post(self):
        parser.add_argument("username")
        parser.add_argument("name")
        parser.add_argument("ig_id")
        parser.add_argument("id")
        parser.add_argument("profile_picture_url")
        parser.add_argument("biography")
        parser.add_argument("follows_count")
        parser.add_argument("followers_count")
        parser.add_argument("media_count")
        args = parser.parse_args()
        data = {k:v for k,v in args.items() if v != None}
        insert_data('users', data)
        data['status'] = 201
        return loads(JSONEncoder().encode(data))

class User(Resource):
    def get(self, username):
        users = get_data('users')
        for dic in users:
            if username == dic['username']:
                return loads(JSONEncoder().encode(dic))
        return {'status': 404}
    def delete(self, username):
        users = get_data('users')
        for dic in users:
            if username == dic['username']:
                delete_data('users', dic)
                return {'status':200}
        return {'status': 404}

class Publication(Resource):
    def get(self):
        parser.add_argument('id', location='args')
        parser.add_argument('username', location='args')
        parser.add_argument('timestamp', location='args')
        parser.add_argument('_id', location='args')
        args = parser.parse_args()
        data = {k:v for k,v in args.items() if v != None}
        return {
        'result': loads(JSONEncoder().encode(get_data('publications', data))),
        'status': 200
        }
    def post(self):
        parser.add_argument('id')
        parser.add_argument('username')
        parser.add_argument('caption')
        parser.add_argument('timestamp')
        parser.add_argument('comments', type=loads, action='append')
        args = parser.parse_args()
        print(args)
        data = {k:v for k,v in args.items() if v != None}
        print(data)
        insert_data('publications', data)
        data['status'] = 201
        return loads(JSONEncoder().encode(data))
    def put(self):
        parser.add_argument('_id')
        parser.add_argument('comments', type=dumps, action='append')
        data = parser.parse_args()
        for i in range(len(data['comments'])):
            data['comments'][i] = loads(data['comments'][i])
        if data['_id'] == None or data['comments'] == None:
            return {'status': 404}
        update_publication(data['comments'], data['_id'])
        query = {"_id": ObjectId(data['_id'])}
        return {
            'result': loads(JSONEncoder().encode(get_data('publications', query))),
            'status': 200
        }