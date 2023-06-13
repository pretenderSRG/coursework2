import json

import pytest
from run import app


class TestApiBlueprint:

    def test_app_return_all_posts(self, correct_keys):
        response = app.test_client().get('/api/posts')
        assert response.status_code == 200
        assert response.content_type == "application/json"
        data = json.loads(response.data)
        assert isinstance(data, list), "Not return list"
        keys_ = set(response.get_json()[0].keys())
        assert keys_ == correct_keys

    def test_app_return_one_post(self, correct_keys):
        response = app.test_client().get('/api/posts/1')
        assert response.status_code == 200
        assert response.content_type == "application/json"
        data = json.loads(response.data)
        assert isinstance(data, dict), "Not return dict"
        keys_ = set(response.get_json().keys())
        assert keys_ == correct_keys
