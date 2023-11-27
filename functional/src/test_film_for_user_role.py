from http import HTTPStatus

import orjson
import pytest

from functional.testdata.movies import SUSPICIOUS_FILM
from functional.utils.sort_filter_movies import (
    sort_movies_by_imdb_rating,
    filter_non_suspicious_movies,
)

DEFAULT_PAGE_SIZE = 20
FILM_NOT_FOUND = 'film not found'
ITEM_DOES_NOT_EXIST = "Item doesn't exist, check if uuid is valid"
ACTION_GENRE_ID = '26a98db2-7267-43b5-bbb3-87be3075d898'
ACTION_SEARCH_RESULT = [
    {
        'uuid': 'cdfe5bf6-e503-4e3d-abff-881b8d077e4e',
        'title': 'Star Fox 64',
        'is_suspicious': False,
        'imdb_rating': 8.6,
    },
    {
        'uuid': 'f640f992-bab3-432c-9339-a7dbbb4d808b',
        'title': 'Star Trek: Beyond the Final Frontier',
        'is_suspicious': False,
        'imdb_rating': 7.3,
    },
    {
        'uuid': '1999ee38-00a0-4287-b316-8d2a88270cda',
        'title': 'Mazzy Star: Fade Into You, Color Version',
        'is_suspicious': False,
        'imdb_rating': 8.1,
    },
    {
        'uuid': '5f3b6455-376b-45b1-8aa6-9404803f6bc2',
        'title': 'Make Me a Star',
        'is_suspicious': False,
        'imdb_rating': 6.5,
    },
]


@pytest.mark.asyncio
async def test_films_list_with_default_query_params(
    make_get_request, all_short_movies
):
    response = await make_get_request('/film')
    assert response.status == HTTPStatus.OK
    assert len(response.body) == DEFAULT_PAGE_SIZE
    assert (
        response.body
        == filter_non_suspicious_movies(
            sort_movies_by_imdb_rating(all_short_movies)
        )[:DEFAULT_PAGE_SIZE]
    )


@pytest.mark.asyncio
async def test_films_list_with_page_size_40(
    make_get_request, all_short_movies
):
    response = await make_get_request('/film/?page[size]=40')
    assert response.status == HTTPStatus.OK
    non_suspicious_movies_sorted_by_rating = sort_movies_by_imdb_rating(
        filter_non_suspicious_movies(all_short_movies)
    )
    assert len(response.body) == len(non_suspicious_movies_sorted_by_rating)
    assert response.body == non_suspicious_movies_sorted_by_rating


@pytest.mark.asyncio
async def test_films_list_with_page_sorted_desc(
    make_get_request, all_short_movies
):
    response = await make_get_request('/film/?sort=imdb_rating')
    assert response.status == HTTPStatus.OK
    assert len(response.body) == DEFAULT_PAGE_SIZE
    assert (
        response.body
        == sort_movies_by_imdb_rating(all_short_movies, False)[
            :DEFAULT_PAGE_SIZE
        ]
    )


@pytest.mark.asyncio
async def test_films_list_second_page(make_get_request, all_short_movies):
    response = await make_get_request('/film/?page[number]=2')
    assert response.status == HTTPStatus.OK
    non_suspicious_movies_sorted_by_rating = sort_movies_by_imdb_rating(
        filter_non_suspicious_movies(all_short_movies)
    )
    assert len(response.body) == len(
        non_suspicious_movies_sorted_by_rating[DEFAULT_PAGE_SIZE:]
    )
    assert (
        response.body
        == non_suspicious_movies_sorted_by_rating[DEFAULT_PAGE_SIZE:]
    )


@pytest.mark.asyncio
async def test_films_list_filtered_by_genre_id(make_get_request):
    response = await make_get_request(
        f'/film/?filter[genre]={ACTION_GENRE_ID}&page[size]=40'
    )
    assert response.status == HTTPStatus.OK
    assert len(response.body) == 3


@pytest.mark.asyncio
async def test_films_list_filtered_by_invalid_genre_id(make_get_request):
    response = await make_get_request('/film/?filter[genre]=abc&page[size]=40')
    assert response.status == HTTPStatus.NOT_FOUND
    assert response.body['detail'] == FILM_NOT_FOUND


@pytest.mark.asyncio
async def test_get_film_by_id(make_get_request, movies):
    response = await make_get_request(f"/film/{movies[0]['_id']}")
    assert response.status == HTTPStatus.OK
    assert response.body == movies[0]['_source']


@pytest.mark.asyncio
async def test_get_film_by_invalid_id(make_get_request):
    response = await make_get_request('/film/abc')
    assert response.status == HTTPStatus.NOT_FOUND
    assert response.body['detail'] == ITEM_DOES_NOT_EXIST


@pytest.mark.asyncio
async def test_search_with_no_value_for_query(make_get_request):
    response = await make_get_request('/film/search/?page[size]=40')
    assert response.status == HTTPStatus.OK
    assert len(response.body) == 4
    assert response.body == ACTION_SEARCH_RESULT


@pytest.mark.asyncio
async def test_search_with_query(make_get_request, all_short_movies):
    response = await make_get_request('/film/search/?query=Star&page[size]=4')
    assert response.status == HTTPStatus.OK
    assert len(response.body) == 4
    assert response.body == filter_non_suspicious_movies(all_short_movies)[:4]


@pytest.mark.asyncio
async def test_search_without_query(make_get_request):
    response = await make_get_request('/film/search/?query=ëç13!&page[size]=5')
    assert response.status == HTTPStatus.NOT_FOUND
    assert response.body['detail'] == FILM_NOT_FOUND


@pytest.mark.asyncio
async def test_data_is_stored_in_redis(
    make_get_request, movies, make_redis_request
):
    await make_get_request(f"/film/{movies[0]['_id']}")
    redis_data = await make_redis_request(movies[0]['_id'])
    item_from_redis = orjson.loads(redis_data)

    assert item_from_redis == movies[0]['_source']


@pytest.mark.asyncio
async def test_user_role_do_not_get_suspicious_film(
    make_get_request, all_short_movies
):
    response = await make_get_request('/film/?page[size]=40')
    assert response.status == HTTPStatus.OK
    assert SUSPICIOUS_FILM not in response.body
