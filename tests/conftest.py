import pytest
from utils.utils import Posts


@pytest.fixture()
def posts():
    return Posts()


@pytest.fixture()
def correct_keys(posts):
    all_posts = posts.get_post_all()
    correct_keys_from_post = set(all_posts[0].keys())
    return correct_keys_from_post


