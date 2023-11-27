from http import HTTPStatus

import pytest

from functional.src.test_film_for_user_role import DEFAULT_PAGE_SIZE
from functional.testdata.movies import SUSPICIOUS_FILM
from functional.utils.sort_filter_movies import sort_movies_by_imdb_rating


@pytest.mark.asyncio
async def test_films_list_with_default_query_params(
    make_get_request, all_short_movies
):
    response = await make_get_request('/film', user_role='admin')
    assert response.status == HTTPStatus.OK
    assert len(response.body) == DEFAULT_PAGE_SIZE
    assert (
        response.body
        == sort_movies_by_imdb_rating(all_short_movies)[:DEFAULT_PAGE_SIZE]
    )


@pytest.mark.asyncio
async def test_films_list_with_page_size_40(
    make_get_request, all_short_movies
):
    response = await make_get_request(
        '/film/?page[size]=40', user_role='admin'
    )
    assert response.status == HTTPStatus.OK
    all_movies_sorted_by_rating = sort_movies_by_imdb_rating(all_short_movies)
    assert len(response.body) == len(all_movies_sorted_by_rating)
    assert response.body == all_movies_sorted_by_rating


@pytest.mark.asyncio
async def test_search_with_query(make_get_request):
    response = await make_get_request(
        '/film/search/?query=Empire of Dreams: The Story of the',
        user_role='admin',
    )
    assert response.status == HTTPStatus.OK
    assert SUSPICIOUS_FILM in response.body
