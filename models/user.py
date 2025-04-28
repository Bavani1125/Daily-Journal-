# models/user.py

from extensions import db
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    name = db.Column(db.String(150), nullable=True)
    profile_pic = db.Column(db.String(300), nullable=True)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # (Optional future fields you can add later)
    # bio = db.Column(db.Text, nullable=True)
    # is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<User {self.email}>'
