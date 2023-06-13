from flask import Blueprint, render_template,request
from utils.utils import Posts, add_tag_to_posts, Bookmarks


main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")
posts = Posts()


@main_blueprint.route('/')
def page_index():
    bookmarks = Bookmarks()
    all_bookmarks_posts = bookmarks.get_all_posts_in_bookmarks()
    all_posts = posts.get_post_all()
    return render_template('index.html', posts=all_posts, bookmarks=all_bookmarks_posts)


@main_blueprint.route('/posts/<int:postid>')
def page_post_id(postid):
    post_by_id = posts.get_post_by_pk(postid)
    content = add_tag_to_posts(post_by_id.get("content"))
    try:
        comments_to_posts = posts.get_comments_by_post_id(postid)
    except ValueError:
        comments_to_posts = {}
    return render_template("post.html", post=post_by_id, comments=comments_to_posts, content=content)


@main_blueprint.route('/search', methods=['GET'])
def search_page():
    s = request.args['s']
    find_posts = posts.search_for_posts(s)
    return render_template("search.html", posts=find_posts)


@main_blueprint.route('/users/<username>', methods=['GET'])
def user_page(username):
    user_posts = posts.get_post_by_user(username)
    return render_template("user-feed.html", posts=user_posts)


@main_blueprint.route('/tag/<tagname>', methods=['GET'])
def tag_page(tagname):
    posts_with_tag = posts.get_posts_by_tag(tagname)
    if posts_with_tag:
        return render_template('tag.html', tag=tagname, posts=posts_with_tag)
    return f"<h1>Постів з тегом #{tagname} - немає((( </h1> <br><a href='/'>На головну</a>", 200


