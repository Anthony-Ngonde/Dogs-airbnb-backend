from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from config import DevConfig
from models import DogHouse
from exts import db


app=Flask(__name__)
app.config.from_object(DevConfig)

db.init_app(app)

api=Api(app)

# Request parser for handling input data for POST and PUT methods
doghouse_parser = reqparse.RequestParser()
doghouse_parser.add_argument('name', type=str, required=True, help="Name of the doghouse is required")
doghouse_parser.add_argument('location', type=str, required=True, help="Location of the doghouse is required")
doghouse_parser.add_argument('description', type=str, required=True, help="Description of the doghouse is required")




class HelloResource(Resource):
    def get(self):
        return{"message":"Hello World"}
    

class DogHousesResource(Resource):

    def get(self):
        """Get all doghouses"""
        doghouses = DogHouse.query.all()

        return jsonify([{
            'id': doghouse.id,
            'name': doghouse.name,
            'location': doghouse.location,
            'description': doghouse.description
        } for doghouse in doghouses])
    
    

    def post(self):
        """Book a doghouse"""
        pass



class DogHouseResource(Resource):
    def get(self,id):
        """Get a doghouse by id"""
        pass

    def put(self,id):
        """Update a doghouse by id"""
        pass

    def delete(self,id):
        """Delete a doghouse by id"""
        pass








    

@app.shell_context_processor
def make_shell_context():
    return {
        "db":db,
        "DogHouse":DogHouse
    }

api.add_resource(HelloResource, '/hello')
api.add_resource(DogHousesResource, '/doghouses')
api.add_resource(DogHouseResource, '/doghouse/<int:id>')
    


if __name__ == '__main':
    app.run()

