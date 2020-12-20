# !usr/bin/env python3

import crypt
import datetime
from flask import flash,g,redirect,render_template,request,session,url_for
import functools
from werkzeug.security import check_password_hash, generate_password_hash

from __init__ import create_app
from database import db,Events,Feelings,Events,Posts,Users

app = create_app()

print(__name__)

@app.route('/',methods=['GET'])
def top():
    user_id = session.get('user_id')
    if user_id is None:
        return redirect(url_for('login'))
    else:
        return redirect(url_for('index',id=user_id))

#User系
@app.route('/signup', methods=('GET','POST'))
def signup():
    if request.method == 'POST':
        name = request.form['username']
        email = request.form['email']
        password = request.form['password']
        error = None
        if not name:
            error = 'Username is required.'
        elif not email:
            error = 'E-mail is required.'
        elif not password:
            error = 'Password is required.'
        elif db.session.query(Users)\
            .filter(Users.email == email)\
            .first() is not None:
            error = 'E-mail {} is already registered.'.format(email)

        print(error)

        if error is None:
            user = Users()
            user.name = name
            user.email = email
            user.password = generate_password_hash(password)
            user.created_at = datetime.datetime.now()
            db.session.add(user)
            db.session.commit()
            user = db.session.query(Users)\
            .filter(Users.email == email)\
            .first()
            return redirect(url_for('index', id=user.id))

        else:
            flash(error)

    return render_template('signup.html')

@app.route('/login', methods=('GET','POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        error = None
        user = db.session.query(Users)\
        .filter(Users.email == email)\
        .first()

        if user is None:
            error = 'メールアドレスが間違っています'
        elif not check_password_hash(user.password, password):
            error = 'パスワードが間違っています'

        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('index', id=user.id))

        flash(error)

    return render_template("login.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('login'))

        return view(**kwargs)

    return wrapped_view

@app.before_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = db.session.query(Users)\
        .filter(Users.id == user_id)\
        .first()

#Post系

@app.route('/<int:id>')
@login_required
def index(id):
    posts = db.session.query(Posts)\
        .filter(Posts.user_id == g.user.id)\
        .outerjoin(Feelings) \
        .outerjoin(Events) \
        .order_by(Posts.id.desc()) \
        .all()
    return render_template("index.html", posts=posts)

@app.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        events = request.form.getlist('event')
        feelings = request.form.getlist('feeling')
        error = None

        if not title:
            error = 'タイトルを50字以内で記入してください'
        elif not content:
            error = '本文を記入してください'

        if error is not None:
            flash(error)
        else:
            post = Posts()
            post.title = title
            post.user_id = g.user.id
            post.content = content
            post.created_at = datetime.datetime.now()
            post.updated_at = datetime.datetime.now()
            db.session.add(post)
            created_post = db.session.query(Posts) \
                .filter(Posts.user_id == g.user.id).order_by(Posts.id.desc()) \
                .first()

            for value in events:
                event = Events()
                event.post_id = int(created_post.id)
                event.event = value
                db.session.add(event)

            for value in feelings:
                feeling = Feelings()
                feeling.post_id = int(created_post.id)
                feeling.feeling = value
                db.session.add(feeling)
            db.session.commit()

            return redirect(url_for('index',id = g.user.id))

    return render_template('create.html')

def get_post(id):
    post = db.session.query(Posts) \
        .filter(Posts.id == id) \
        .first()
    return post

@app.route('/update/<int:id>', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        error = None

        if not title:
                error = 'タイトルを50字以内で記入してください'
        elif not content:
                error = '本文を記入してください'

        if error is not None:
                flash(error)
        else:
            time = datetime.datetime.now()
            post.title = title
            post.content = content
            post.updated_at = time
            db.session.commit()
            return redirect(url_for('index',id = g.user.id))

    return render_template('update.html', post=post)

@app.route('/delete/<int:id>', methods=('POST',))
@login_required
def delete(id):
    db.session.query(Feelings) \
        .filter(Feelings.post_id == id) \
        .delete()
    db.session.query(Events) \
        .filter(Events.post_id == id) \
        .delete()
    db.session.query(Posts) \
        .filter(Posts.id == id) \
        .one()
    db.session.commit()
    return redirect(url_for('index',id = g.user.id))

if __name__ == '__main__':
  app.run()