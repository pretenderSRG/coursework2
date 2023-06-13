from flask import Blueprint, render_template,request
from utils.utils import Posts


main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")
posts = Posts()


@main_blueprint.route('/')
def page_index():
    all_posts = posts.get_post_all()
    return render_template('index.html', posts=all_posts)


@main_blueprint.route('/posts/<int:postid>')
def page_post_id(postid):
    post_by_id = posts.get_post_by_pk(postid)
    try:
        comments_to_posts = posts.get_comments_by_post_id(postid)
    except ValueError:
        comments_to_posts = {}
    return render_template("post.html", posts=post_by_id, comments=comments_to_posts)


@main_blueprint.route('/search', methods=['GET'])
def search_page():
    s = request.args['s']
    find_posts = posts.search_for_posts(s)
    return render_template("search.html", posts=find_posts)


@main_blueprint.route('/users/<username>')
def user_page(username):
    user_posts = posts.get_post_by_user(username)
    return render_template("user-feed.html", posts=user_posts)
