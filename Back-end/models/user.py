# models/user.py

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def _repr_(self):
        return f"<User {self.username}>"

    def guardar(self):
            db.session.add(self)
            db.session.commit()