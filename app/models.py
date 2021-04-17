from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from app import app

db = SQLAlchemy(app)

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    hospital_id = db.Column(db.Integer, db.ForeignKey('hospital.id'), nullable=False)

    def __repr__(self):
        return '<Patient %r>' % self.first_name + ' ' + self.last_name

class Hospital(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    patients = db.relationship('Patient', backref='hospital', lazy=True)

    def __repr__(self):
        return '<Hospital %r>' % self.name
