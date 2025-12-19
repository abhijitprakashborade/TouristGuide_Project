from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    itineraries = db.relationship('Itinerary', backref='author', lazy='dynamic')
    feedbacks = db.relationship('Feedback', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.username}>'

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class Place(db.Model):
    __tablename__ = 'places'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    description = db.Column(db.Text)
    category = db.Column(db.String(64)) # Museum, Park, Historical, etc.
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    location_address = db.Column(db.String(256))
    entry_fee = db.Column(db.Float, default=0.0)
    image_file = db.Column(db.String(128), default='default_place.jpg')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    feedbacks = db.relationship('Feedback', backref='place', lazy='dynamic')

    def __repr__(self):
        return f'<Place {self.name}>'

class Itinerary(db.Model):
    __tablename__ = 'itineraries'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(128), default="My Trip")
    preferences_snapshot = db.Column(db.Text) # JSON string of prefs used to generate
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Store ordered place IDs as a simple way to keep the sequence
    # In a real app, a many-to-many association table with 'order' column is better
    # For simplicity here: "1,4,2,8"
    place_ids = db.Column(db.String(256)) 

    def __repr__(self):
        return f'<Itinerary {self.id} for User {self.user_id}>'

class Feedback(db.Model):
    __tablename__ = 'feedbacks'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    place_id = db.Column(db.Integer, db.ForeignKey('places.id'))
    rating = db.Column(db.Integer) # 1-5
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Feedback {self.rating} for Place {self.place_id}>'
