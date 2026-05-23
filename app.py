from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    genre = db.Column(db.String(100))
    rating = db.Column(db.String(10))
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)


@app.route('/create_movie', methods=['GET', 'POST'])
def create_movie():
    if request.method == 'POST':
        name = request.form.get('name')
        genre = request.form.get('genre')
        rating = request.form.get('rating')

        movie = Movie(name=name, genre=genre, rating=rating)
        db.session.add(movie)
        db.session.commit()

        return redirect('/create_movie')
      
    return render_template('create_movie.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
