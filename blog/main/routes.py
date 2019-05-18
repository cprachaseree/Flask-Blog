from flask import Blueprint, render_template, request
from blog.models import Post

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    # get all of the posts in the database use posts = Post.query.all()
    # posts seperated into pages
    page = request.args.get('page', default=1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=8)
    return render_template('home.html', posts=posts)

@main.route("/about")
def about():
    return render_template('about.html')
