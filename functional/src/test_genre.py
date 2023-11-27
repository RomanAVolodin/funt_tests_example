import orjson
import pytest
from http import HTTPStatus

from functional.testdata.genres import (
    GENRES_RESPONSE,
    GENRES_RESPONSE_SORTED_NAME_ASC,
    GENRES_RESPONSE_SORTED_NAME_DESC,
)

SORT_BY_NAME_MESSAGE = 'You can sort ONLY by fields: name'
GENRES_NOT_FOUND_MESSAGE = 'genres not found'
ITEM_DOESNT_EXIST_MESSAGE = "Item doesn't exist, check if uuid is valid"


@pytest.mark.asyncio
async def test_genres_list(make_get_request, genres):
    response = await make_get_request('/genre')
    assert response.status == HTTPStatus.OK
    assert len(response.body) == len(genres)
    assert GENRES_RESPONSE[0] in response.body


@pytest.mark.asyncio
async def test_sort_by_name_desc(make_get_request):
    response = await make_get_request('/genre/?sort=-name')
    assert response.status == HTTPStatus.OK
    assert (
        response.body[0]['name'] == GENRES_RESPONSE_SORTED_NAME_DESC[0]['name']
    )


@pytest.mark.asyncio
async def test_sort_by_name_asc(make_get_request):
    response = await make_get_request('/genre/?sort=name')
    assert response.status == HTTPStatus.OK
    assert (
        response.body[0]['name'] == GENRES_RESPONSE_SORTED_NAME_ASC[0]['name']
    )


@pytest.mark.asyncio
async def test_sort_by_incorrect_field(make_get_request):
    response = await make_get_request('/genre/?sort=some_wrong_name')
    assert response.status == HTTPStatus.BAD_REQUEST
    assert response.body['detail'] == SORT_BY_NAME_MESSAGE


@pytest.mark.asyncio
async def test_list_only_three_genres(make_get_request):
    response = await make_get_request('/genre/?page[size]=3&page[number]=1')
    assert response.status == HTTPStatus.OK
    assert len(response.body) == 3
    assert response.body == GENRES_RESPONSE[:3]


@pytest.mark.asyncio
async def test_list_all_query_params(make_get_request):
    response = await make_get_request(
        '/genre/?page[size]=3&page[number]=2&sort=-name'
    )
    assert response.status == HTTPStatus.OK
    assert len(response.body) == 3
    assert response.body == GENRES_RESPONSE_SORTED_NAME_DESC[3:6]


@pytest.mark.asyncio
async def test_list_with_search(make_get_request):
    response = await make_get_request(
        f'/genre/?query={GENRES_RESPONSE[0]["name"]}'
    )
    assert response.status == HTTPStatus.OK
    assert len(response.body) == 1
    assert GENRES_RESPONSE[0] in response.body


@pytest.mark.asyncio
async def test_list_with_search_wrong_name(make_get_request):
    response = await make_get_request('/genre/?query=wrong_name')
    assert response.status == HTTPStatus.NOT_FOUND
    assert response.body['detail'] == GENRES_NOT_FOUND_MESSAGE


@pytest.mark.asyncio
async def test_fetch_exact_genre_by_id(make_get_request):
    response = await make_get_request(f'/genre/{GENRES_RESPONSE[0]["uuid"]}')
    assert response.status == HTTPStatus.OK
    assert response.body == GENRES_RESPONSE[0]


@pytest.mark.asyncio
async def test_fetch_genre_by_wrong_id(make_get_request):
    response = await make_get_request('/genre/any_string')
    assert response.status == HTTPStatus.NOT_FOUND
    assert response.body['detail'] == ITEM_DOESNT_EXIST_MESSAGE


@pytest.mark.asyncio
async def test_redis_stored_data(make_get_request, make_redis_request):
    await make_get_request(f'/genre/{GENRES_RESPONSE[0]["uuid"]}')

    redis_data = await make_redis_request(GENRES_RESPONSE[0]['uuid'])
    item_from_redis = orjson.loads(redis_data)

    assert item_from_redis['name'] == GENRES_RESPONSE[0]['name']
    assert item_from_redis['uuid'] == GENRES_RESPONSE[0]['uuid']
