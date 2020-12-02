
import functools
from flask import Blueprint,flash,g,redirect,render_template,request,session,url_for
from werkzeug.security import check_password_hash, generate_password_hash
import datetime

from ..database import db
from ..models.users import Users

# set route
user = Blueprint('user_router', __name__)

@user.route('/signup', methods=('GET','POST'))
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
            return redirect(url_for('post_router.index', id=user.id))

        else:
            flash(error)

    return render_template('signup.html')

@user.route('/login', methods=('GET','POST'))
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
            return redirect(url_for('post_router.index', id=user.id))

        flash(error)

    return render_template("login.html")

@user.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = db.session.query(Users)\
        .filter(Users.id == user_id)\
        .first()

@user.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('user_router.login'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('user_router.login'))

        return view(**kwargs)

    return wrapped_view