from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    file_name = db.Column(db.String(255), nullable=False)
    clothingtype = db.Column(db.String(255), nullable=False)
    colour = db.Column(db.String(255), nullable=False)