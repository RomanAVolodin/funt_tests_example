import pytest

from functional.testdata.movies import MOVIES
from functional.testdata.people import MOVIES_FOR_PEOPLE


@pytest.fixture
def movies():
    return MOVIES


@pytest.fixture
def movies_for_people():
    return MOVIES_FOR_PEOPLE


@pytest.fixture
def all_movies():
    return merge_of_two_lists(MOVIES, MOVIES_FOR_PEOPLE)


@pytest.fixture
def all_short_movies():
    all_movies = merge_of_two_lists(MOVIES, MOVIES_FOR_PEOPLE)
    return [
        {
            'uuid': d['_source']['uuid'],
            'title': d['_source']['title'],
            'is_suspicious': d['_source']['is_suspicious'],
            'imdb_rating': d['_source']['imdb_rating'],
        }
        for d in all_movies
    ]


def merge_of_two_lists(lst1, lst2):
    lst1_copy = lst1.copy()
    lst1_copy.extend(lst2)
    return lst1_copy
