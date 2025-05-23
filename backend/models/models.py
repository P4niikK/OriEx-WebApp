from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    shipments = db.relationship('Shipment', backref='user', lazy=True)

    def check_password(self, password, bcrypt):
        return bcrypt.check_password_hash(self.password_hash, password)

    def set_password(self, password, bcrypt):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

class Shipment(db.Model):
    __tablename__ = 'shipments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    tracking_id = db.Column(db.String(50), unique=True, nullable=False)
    origin_address_china = db.Column(db.Text, nullable=False)
    destination_address_argentina = db.Column(db.Text, nullable=False)
    weight_kg = db.Column(db.Numeric(10, 2), nullable=False)
    client_price_per_kg_usd = db.Column(db.Numeric(10, 2), nullable=False)
    total_client_price_usd = db.Column(db.Numeric(10, 2), nullable=False)
    our_profit_per_kg_usd = db.Column(db.Numeric(10, 2), nullable=False)
    total_profit_usd = db.Column(db.Numeric(10, 2), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    estimated_delivery_date = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    notes = db.Column(db.Text)
