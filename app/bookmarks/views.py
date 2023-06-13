from flask import Blueprint, render_template, redirect
from utils.utils import Posts, Bookmarks

posts = Posts()
bookmarks = Bookmarks()


bookmarks_bp = Blueprint("bookmarks_bp", __name__, url_prefix='/bookmarks', template_folder='templates')


@bookmarks_bp.route('/', methods=['GET'])
def bookmarks_page():
    bookmarks_posts = bookmarks.get_all_posts_in_bookmarks()
    if not bookmarks_posts:
        return "<h1>Список закладок порожній</h1><br><a href='/'><strong>На головну</strong></a>"
    return render_template('bookmarks.html', bookmarks=bookmarks_posts)


@bookmarks_bp.route('/add/<int:postid>', methods=['GET'])
def add_bookmarks_posts(postid):
    all_posts = posts.get_post_all()
    post_by_id = posts.get_post_by_pk(postid)
    bookmarks.add_post_to_bookmark(post_by_id)
    return redirect("/", code=302)


@bookmarks_bp.route('/remove/<int:postid>')
def remove_bookmarks_post(postid):
    all_bookmarks = bookmarks.get_all_posts_in_bookmarks()
    for post in all_bookmarks:
        if post.get("pk") == postid:
            bookmarks.remove_post_from_bookmark(postid)
    return redirect('/bookmarks', code=302)
