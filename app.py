from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from config import DevConfig
from models import DogHouse
from exts import db
from flask_migrate import Migrate


app=Flask(__name__)
app.config.from_object(DevConfig)

db.init_app(app)

migrate = Migrate(app,db)

api=Api(app)

# Request parser for handling input data for POST and PUT methods
doghouse_parser = reqparse.RequestParser()
doghouse_parser.add_argument('name', type=str, required=True, help="Name of the doghouse is required")
doghouse_parser.add_argument('location', type=str, required=True, help="Location of the doghouse is required")
doghouse_parser.add_argument('description', type=str, required=True, help="Description of the doghouse is required")




class HelloResource(Resource):
    def get(self):
        return{"message":"Hello World"}
    
@api.route('/signup')
class SignUp(Resource):
    def post(self):
        pass

@api.route('/login')
class Login(Resource):
    def post(self):
        pass
    

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
        args = doghouse_parser.parse_args()
        new_doghouse = DogHouse(
            name = args['name'],
            location = args['location'],
            description = args['description']
        )

        db.session.add(new_doghouse)
        db.session.commit()
        return {"message": "Doghouse booked successfully"}



class DogHouseResource(Resource):
    def get(self,id):
        """Get a doghouse by id"""
        doghouse = DogHouse.query.get_or_404(id)
        return jsonify({
            'id': doghouse.id,
            'name': doghouse.name,
            'location': doghouse.location,
            'description': doghouse.description
        })
    

    def put(self,id):
        """Update a doghouse by id"""
        args = doghouse_parser.parse_args()
        doghouse = DogHouse.query.get_or_404(id)
        doghouse.name = args['name']
        doghouse.location = args['location']
        doghouse.description = args['description']
        db.session.commit()
        return {"message": "Doghouse updated successfully"}



    def delete(self,id):
        """Delete a doghouse by id"""
        doghouse = DogHouse.query.get_or_404(id)
        db.session.delete(doghouse)
        db.session.commit()
        return {"message": "Doghouse deleted successfully"}








    

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

