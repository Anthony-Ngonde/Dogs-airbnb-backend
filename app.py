from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from config import DevConfig
from models import User
from exts import db
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, jwt_required
from resources.doghouses import DogHousesResource, DogHouseResource
from resources.reviews import ReviewsResource, ReviewResource
from resources.bookings import BookingsResource, BookingResource
from resources.auth import SignUp, Login, HelloResource




def create_app(config_class=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate = Migrate(app, db)
    JWTManager(app)

    api = Api(app)

    
    api.add_resource(HelloResource, '/hello')
    
    # Add resources
    api.add_resource(SignUp, '/signup')
    api.add_resource(Login, '/login')

    # Routes for DogHouses
    api.add_resource(DogHousesResource, '/doghouses')
    api.add_resource(DogHouseResource, '/doghouse/<int:id>')

    # Routes for Reviews
    api.add_resource(ReviewsResource, '/reviews')
    api.add_resource(ReviewResource, '/reviews/<int:id>')

    # Routes for Bookings
    api.add_resource(BookingsResource, '/bookings')
    api.add_resource(BookingResource, '/bookings/<int:id>')

    return app

