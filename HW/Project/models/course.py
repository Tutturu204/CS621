from app import db


class Course(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable=False)
    professor = db.Column(db.String(50), nullable=False)
    semester = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(400), nullable=True)
    
    def __repr__(self):
        return f"Course('{self.id}', '{self.name}', '{self.professor}', '{ self.semester}', '{ self.score}', '{self.weight}', '{self.description}')"
        