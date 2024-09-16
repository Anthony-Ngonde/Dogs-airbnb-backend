from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token
from models import User
from exts import db

# Request parser for handling sign-up data
signup_parser = reqparse.RequestParser()
signup_parser.add_argument('username', type=str, required=True, help="Username is required")
signup_parser.add_argument('email', type=str, required=True, help="Email is required")
signup_parser.add_argument('password', type=str, required=True, help="Password is required")


# Request parser for handling login data
login_parser = reqparse.RequestParser()
login_parser.add_argument('username', type=str, required=True, help="Username is required")
login_parser.add_argument('password', type=str, required=True, help="Password is required")



class HelloResource(Resource):
    def get(self):
        return {"message": "Hello World"}
    


class SignUp(Resource):
    def post(self):
        data = signup_parser.parse_args()

        username = data['username']
        email = data['email']
        password = data['password']

        # Check if user already exists
        db_user = User.query.filter_by(username=username).first()

        if db_user is not None:
            return {"message": f"User with username {username} already exists"}, 400
        
        # Create new user
        hashed_password = generate_password_hash(password)
        new_user = User(
            username = username,
            email = email,
            password = hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        return {
            "message": "User created successfully",
            # "user": {
            #     "username": new_user.username,
            #     "email": new_user.email,
            #     "password": new_user.password
            # }
        }, 201
    

class Login(Resource):
    def post(self):
        data = login_parser.parse_args()

        username = data['username']
        password = data['password']

        # Find the user by username
        db_user = User.query.filter_by(username=username).first()

        if db_user and check_password_hash(db_user.password, password):
            # Generate JWT tokens
            access_token = create_access_token(identity=db_user.username)
            refresh_token = create_refresh_token(identity=db_user.username)
            # Return the tokens
            return {
                "access_token": access_token,
                "refresh_token": refresh_token
            }, 200
        
        # Invalid login
        return {"message": "Invalid username or password"}, 401

    


