from flask import Flask, Blueprint, jsonify, request
import logging
from utils.utils import Posts

api_blueprint = Blueprint("api_blueprint", __name__, url_prefix="/api")
posts = Posts()

FORMAT = "%(asctime)s [%(levelname)s] %(message)s "
logger = logging.getLogger("api_blueprint")
logger.setLevel(logging.INFO)
handler = logging.FileHandler("app/api/api.log", mode='w', encoding="utf-8")
formatter = logging.Formatter(FORMAT)
logger.addHandler(handler)
handler.setFormatter(formatter)


@api_blueprint.route('/posts')
def return_all_posts():
    logger.info(f"Запит {request.path}")
    all_posts = posts.get_post_all()
    return jsonify(all_posts)


@api_blueprint.route('/posts/<int:post_id>')
def return_post_by_id(post_id):
    logger.info(f"Запит {request.path}")
    post = posts.get_post_by_pk(post_id)
    if post:
        return jsonify(post)
    return jsonify({"error": "Post not found"}), "404"
