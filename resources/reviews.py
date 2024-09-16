from flask import jsonify
from flask_restful import Resource, reqparse
from models import Review
from exts import db
from flask_jwt_extended import jwt_required

# Request parser for handling input data for POST and PUT methods
review_parser = reqparse.RequestParser()
review_parser.add_argument('doghouse_id', type=int, required=True, help="Doghouse ID is required")
review_parser.add_argument('user_id', type=int, required=True, help="User ID is required")
review_parser.add_argument('rating', type=int, required=True, help="Rating is required")
review_parser.add_argument('comment', type=str, required=True, help="Comment is required")

class ReviewsResource(Resource):

    def get(self):
        """Get all reviews"""
        reviews = Review.query.all()

        return jsonify([{
            'id': review.id,
            'doghouse_id': review.doghouse_id,
            'user_id': review.user_id,
            'rating': review.rating,
            'comment': review.comment

        } for review in reviews])
    
    jwt_required()
    def post(self):
        """Post a review"""
        args = review_parser.parse_args()
        new_review = Review(
            doghouse_id = args['doghouse_id'],
            user_id = args['user_id'],
            rating = args['rating'],
            comment = args['comment']
        )

        db.session.add(new_review)
        db.session.commit()
        return {"message": "Review posted successfully"}
    

class ReviewResource(Resource):
    def get(self, id):
        """Get a review by id"""
        review = Review.query.get_or_404(id)
        return jsonify({
            'id': review.id,
            'doghouse_id': review.doghouse_id,
            'user_id': review.user_id,
            'rating': review.rating,
            'comment': review.comment
            })
    
    # @jwt_required()
    def put(self, id):
        """Update a review by id"""
        args = review_parser.parse_args()
        review = Review.query.get_or_404(id)
        review.doghouse_id = args['doghouse_id']
        review.user_id = args['user_id']
        review.rating_id = args['rating']
        review.comment = args['comment']
        db.session.commit()
        return {"message": "Review updated successfully"}
    
    # @jwt_required()
    def delete(self, id):
        """Delete a review by id"""
        review = Review.query.get_or_404(id)
        db.session.delete(review)
        db.session.commit()
        return {"message": "Review deleted successfully"}
