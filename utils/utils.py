import json


class Posts:

    @staticmethod
    def __get_post_all() -> list:
        """
        Get all post from json file
        :return: list with data
        """
        with open("data/posts.json", "r", encoding="utf-8") as file:
            all_posts = json.load(file)
        return all_posts

    @staticmethod
    def __get_comments_all():
        with open("data/comments.json", "r", encoding="utf-8") as file:
            all_comments = json.load(file)
        return all_comments

    def get_post_by_user(self, user_name: str) -> list:
        """
        Get all posts by user
        :param user_name: name of user
        :return: List with all post of the user
        """
        all_posts = self.__get_post_all()
        all_posts_by_user = []
        flag = False
        for post in all_posts:
            if post.get("poster_name") == user_name.lower():
                all_posts_by_user.append(post)
                flag = True
        if flag:
            raise ValueError("User not found")
        return all_posts_by_user

    def get_comments_by_post_id(self, post_id: int) -> list:
        """
        Gett all coments to post by id
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
            raise ValueError("Comments no found")
        return comments_by_post_id

    def search_for_posts(self, query: str) -> list:
        """
        Return all searching posts
        :param query: parameter search
        :return:
        """
        all_posts = self.__get_post_all()
        searching_posts = []
        for post in all_posts:
            if query.lower() in post.get("content").lower():
                searching_posts.append(post)
        return searching_posts

    def get_post_by_pk(self, pk:int) -> dict | None:
        all_posts = self.__get_post_all()
        for post in all_posts:
            if post.get("pk") == pk:
                return post
        return None
