from flask import Blueprint,flash,g,redirect,render_template,request,session,url_for
import datetime

from ..views.user import login_required
from ..database import db
from ..models.posts import Events,Feelings,Posts
from ..models.users import Users

post = Blueprint('post_router', __name__)

@post.route('/<int:id>')
def index(id):
    posts = db.session.query(Posts)\
        .filter(Posts.user_id == g.user.id)\
        .join(Feelings, Posts.id == Feelings.post_id) \
        .join(Events, Posts.id == Events.post_id) \
        .all()
    return render_template("index.html", posts=posts)

@post.route('/create', methods=('GET', 'POST'))
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

            return redirect(url_for('post_router.index',id = g.user.id))

    return render_template('create.html')

def get_post(id):
    post = db.session.query(Posts) \
        .filter(Posts.id == id) \
        .first()
    return post

@post.route('/update/<int:id>', methods=('GET', 'POST'))
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
            return redirect(url_for('post_router.index',id = g.user.id))

    return render_template('update.html', post=post)

@post.route('/delete/<int:id>', methods=('POST',))
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
    return redirect(url_for('post_router.index',id = g.user.id))