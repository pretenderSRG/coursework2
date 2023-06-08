import pytest
from utils.utils import Posts


@pytest.fixture()
def posts():
    return Posts()
