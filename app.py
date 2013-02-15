from flask import Flask
from flask import *
from models import *
from flask.ext.admin import Admin, BaseView, expose
from flask.ext.admin.contrib.sqlamodel import ModelView
from flask.ext.admin.contrib.fileadmin import FileAdmin
import os.path as op

app = Flask(__name__)

@app.route("/")
@app.route("/books")
def books():
	authors = Author.query.order_by('Author.name')
	return render_template('index.html',authors=authors)

@app.route("/book/<int:book_id>")
def book(book_id=None):
	book = Book.query.get(book_id)
	return render_template('book.html',book=book)

@app.route('/author/<int:author_id>')
def author(author_id=None):
	author = Author.query.get(author_id)
	return render_template('author.html', author=author)

admin = Admin(app)
admin.add_view(ModelView(Author, db.session))
admin.add_view(ModelView(Book, db.session))

path = op.join(op.dirname(__file__), 'static')
admin.add_view(FileAdmin(path, '/static/', name='Static Files'))

app.secret_key = 'this is my secret'

if __name__ == "__main__":
	app.run(debug=True, port=5000, host='0.0.0.0')