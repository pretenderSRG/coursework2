from flask import Blueprint, render_template
from utils.utils import Posts


main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")
posts = Posts()


@main_blueprint.route('/')
def page_index():
    all_posts = posts.get_post_all()
    return render_template('index.html', posts=all_posts)
