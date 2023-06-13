import json


def add_tag_to_posts(content: str) -> str:
    content_words = content.split()
    content_with_life_tag = []
    for word in content_words:
        if word.startswith("#"):
            content_with_life_tag.append(f"<a href='/tag/{word[1:]}'>{word}</a>")
        else:
            content_with_life_tag.append(word)
    return ' '.join(content_with_life_tag)


class Posts:

    PATH_TO_POSTS = "data/posts.json"
    PATH_TO_COMMENTS = "data/comments.json"

    @staticmethod
    def get_post_all() -> list:
        """
        Get all post from json file
        :return: list with data
        """
        try:
            with open(Posts.PATH_TO_POSTS, "r", encoding="utf-8") as file:
                all_posts = json.load(file)
        except FileNotFoundError:
            all_posts = []

        except json.JSONDecodeError:
            all_posts = []
        return all_posts

    @staticmethod
    def __get_comments_all():
        try:
            with open(Posts.PATH_TO_COMMENTS, "r", encoding="utf-8") as file:
                all_comments = json.load(file)
        except FileNotFoundError:
            return None
        return all_comments

    def get_post_by_user(self, user_name: str) -> list:
        """
        Get all posts by user
        :param user_name: name of user
        :return: List with all post of the user
        """
        all_posts = self.get_post_all()
        all_posts_by_user = []
        flag = False
        for post in all_posts:
            if post.get("poster_name") == user_name.lower():
                all_posts_by_user.append(post)
                flag = True
        if not flag:
            raise ValueError("User not found")
        return all_posts_by_user

    def get_comments_by_post_id(self, post_id: int) -> list:
        """
        Get all comments to post by id
        :param post_id: post id
        :return: all comments
        """
        all_comments = self.__get_comments_all()
        comments_by_post_id = []
        flag = False
        for comment in all_comments:
            if comment.get("post_id") == post_id:
                comments_by_post_id.append(comment)
                flag = True
        if flag:
            return comments_by_post_id
        raise ValueError("Comments not found")

    def search_for_posts(self, query: str) -> list:
        """
        Return all searching posts
        :param query: parameter search
        :return:
        """
        all_posts = self.get_post_all()
        searching_posts = []
        for post in all_posts:
            if query.lower() in post.get("content").lower():
                searching_posts.append(post)
        return searching_posts

    def get_post_by_pk(self, pk: int) -> dict | None:
        all_posts = self.get_post_all()
        for post in all_posts:
            if post.get("pk") == pk:
                return post
        return None

    def get_posts_by_tag(self, tag):
        all_posts = self.get_post_all()
        tagname = "#" + tag
        posts_with_tag = []

        for post in all_posts:
            content_word = post.get("content").split()
            if tagname in content_word:
                posts_with_tag.append(post)
        return posts_with_tag
