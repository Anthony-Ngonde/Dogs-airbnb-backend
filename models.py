from exts import db

"""
class DogHouse:
    id:int primary key
    name:str
    location:str
    description:str (text)
"""

class DogHouse(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    name=db.Column(db.String(), nullable=False)
    location=db.Column(db.String(), nullable=False)
    description=db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return f"<DogHouse {self.name}>"
    
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

