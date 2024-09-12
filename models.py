from exts import db

"""
class DogHouse:
    id:int primary key
    name:str
    location:str
    description:str (text)
"""

# user model
"""
class User:
    id:integer
    username:string
    email:string
    password:string

"""

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable = False, unique=True)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"




class DogHouse(db.Model):
    __tablename__ = 'doghouses'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    location = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return f"<DogHouse {self.name}>"
    

class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    doghouse_id = db.Column(db.Integer(), db.ForeignKey('doghouses.id'), nullable=False)
    rating = db.Column(db.Integer(), nullable=False)
    comment = db.Column(db.Text, nullable=False)

class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    doghouse_id = db.Column(db.Integer, db.ForeignKey('doghouses.id'), nullable=False)
    check_in_date = db.Column(db.Date, nullable = False)
    check_out_date = db.Column(db.Date, nullable=False)


    





    
    # def save(self):
    #     db.session.add(self)
    #     db.session.commit()
    
    # def delete(self):
    #     db.session.delete(self)
    #     db.session.commit()
    
    # def update(self, name, location, description):
    #     self.name=name
    #     self.description=description

    #     db.session.commit()

