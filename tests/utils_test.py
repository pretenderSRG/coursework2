import pytest


class TestPosts:

    def test_get_post_all_return_list(self, posts):
        all_posts = posts.get_post_all()
        assert isinstance(all_posts, list), "Does not return a list"

    def test_get_post_all_file_not_found(self, monkeypatch, posts):
        def mock_open(*args, **kwargs):
            raise FileNotFoundError

        monkeypatch.setattr("builtins.open", mock_open)
        all_posts = posts.get_post_all()
        assert all_posts == []

    def test_get_post_by_user_return_list(self, posts):
        posts_by_name = posts.get_post_by_user("leo")
        assert isinstance(posts_by_name, list)

    def test_get_post_by_user_correct(self, posts):
        correct_user_name = posts.get_post_by_user("leo")
        assert correct_user_name[0].get("poster_avatar") == "https://meragor.com/getavatar?i=public%3A%2F%2Favatar-222329-077785.png&w=200&h=200"

    def test_get_post_by_user_wrong_user(self, posts):
        with pytest.raises(ValueError):
            one_user_post = posts.get_post_by_user("lord")

    def test_get_comments_all_return_list(self, posts):
        get_all_comments = getattr(posts, "_Posts__get_comments_all")
        all_comments = get_all_comments()
        assert isinstance(all_comments, list)

    # def test_get_comments_all_file_not_found(self, posts, monkeypatch):
    #     def mock_open(*args, **kwargs):
    #         return FileNotFoundError
    #     monkeypatch.setattr("builtins.open", mock_open)
    #     get_all_comments = getattr(posts, "_Posts__get_comments_all")
    #     all_comments = get_all_comments()
    #     assert all_comments == []
    def test_get_comments_by_post_id_return_list(self, posts):
        comments_by_post_id_1 = posts.get_comments_by_post_id(1)
        assert isinstance(comments_by_post_id_1, list)

    def test_get_post_by_pk_return_dict(self, posts):
        post_by_pk_1 = posts.get_post_by_pk(1)
        assert isinstance(post_by_pk_1, dict)

    def test_search_for_posts_return_list(self, posts):
        result = posts.search_for_posts("a")
        assert isinstance(result, list)

    def test_get_post_by_pk_incorrect_pk(self, posts):
        posts_by_wrong_pk = posts.get_post_by_pk(-1)
        assert posts_by_wrong_pk is None



