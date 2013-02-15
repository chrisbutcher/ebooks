from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/chris/py/ebooks/dev.db'
db = SQLAlchemy(app)

class Author(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	books = db.relationship('Book', backref='author', lazy='dynamic')

	def __repr__(self):
		return self.name

class Book(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(128), unique=True)
	cover_url = db.Column(db.String(2048))
	file_txt_url = db.Column(db.String(2048))
	author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

	def __repr__(self):
		return self.title