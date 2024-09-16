from flask import jsonify
from flask_restful import Resource, reqparse
from models import Booking
from exts import db
from flask_jwt_extended import jwt_required
from datetime import datetime

# Request parser for handling input data for POST and PUT methods
booking_parser = reqparse.RequestParser()
booking_parser.add_argument('user_id', type=int, required=True, help="User ID is required")
booking_parser.add_argument('doghouse_id', type=int, required=True, help="Doghouse ID is required")
booking_parser.add_argument('check_in_date', type=str, required=True, help="Check-in date is required")
booking_parser.add_argument('check_out_date', type=str, required=True, help="Check-out date is required")

class BookingsResource(Resource):
    def get(self):
        """Get all bookings"""
        bookings = Booking.query.all()

        return jsonify([{
            'id': booking.id,
            'user_id': booking.user_id,
            'doghouse_id': booking.doghouse_id,
            'check_in_date': booking.check_in_date,
            'check_out_date': booking.check_out_date
            } for booking in bookings])
    
    # @jwt_required()
    def post(self):
        """Create a booking"""
        args = booking_parser.parse_args()

        new_booking = Booking(
            user_id = args['user_id'],
            doghouse_id = args['doghouse_id'],
            check_in_date = datetime.strptime(args['check_in_date'], '%Y-%m-%d'),
            check_out_date = datetime.strptime(args['check_out_date'], '%Y-%m-%d')
        )

        db.session.add(new_booking)
        db.session.commit()
        return {"message": "Booking created successfully"}
    

class BookingResource(Resource):
    def get(self, id):
        """Get a booking by id"""
        booking = Booking.query.get_or_404(id)
        return jsonify({
            'id': booking.id,
            'user_id':booking.user_id,
            'doghouse_id':booking.doghouse_id,
            'check_in_date': booking.check_in_date,
            'check_out_date': booking.check_out_date
        })
    
    # @jwt_required()
    def put(self, id):
        """Update a booking by id"""
        args = booking_parser.parse_args()
        booking = Booking.query.get_or_404(id)
        booking.user_id = args['user_id']
        booking.doghouse_id = args['doghouse_id']
        booking.check_in_date = datetime.strptime(args['check_in_date'], '%Y-%m-%d')
        booking.check_out_date = datetime.strptime(args['check_out_date'], '%Y-%m-%d')
        db.session.commit()
        return {"message": "Booking updated successfully"}
    
    # @jwt_required()
    def delete(self, id):
        """Delete a booking by id"""
        booking = Booking.query.get_or_404(id)
        db.session.delete(booking)
        db.session.commit()
        return {"message": "Booking deleted successfully"}