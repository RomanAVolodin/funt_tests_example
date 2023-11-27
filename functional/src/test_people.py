from http import HTTPStatus

import orjson
import pytest

from functional.testdata.people import (
    PEOPLE_RESPONSE,
    PEOPLE_RESPONSE_SORTED_NAME_ASC,
    PEOPLE_RESPONSE_SORTED_NAME_DESC,
    MOVIES_RESPONSE,
)


SORT_BY_NAME_MESSAGE = 'You can sort ONLY by fields: full_name'
PERSON_NOT_FOUND_MESSAGE = 'people or person not found'
ITEM_DOESNT_EXIST_MESSAGE = "Item doesn't exist, check if uuid is valid"
FILMS_FOR_PERSON_NOT_FOUND_MESSAGE = 'films for person not found'


@pytest.mark.asyncio
async def test_people_list(make_get_request, people):
    response = await make_get_request('/person/search/')
    assert response.status == HTTPStatus.OK
    assert len(response.body) == len(people)
    assert PEOPLE_RESPONSE[0] in response.body


@pytest.mark.asyncio
async def test_sort_by_name_desc(make_get_request):
    response = await make_get_request('/person/search/?sort=-full_name')
    assert response.status == HTTPStatus.OK
    assert response.body[0] == PEOPLE_RESPONSE_SORTED_NAME_DESC[0]


@pytest.mark.asyncio
async def test_sort_by_name_asc(make_get_request):
    response = await make_get_request('/person/search/?sort=full_name')
    assert response.status == HTTPStatus.OK
    assert response.body[0] == PEOPLE_RESPONSE_SORTED_NAME_ASC[0]


@pytest.mark.asyncio
async def test_sort_by_incorrect_field(make_get_request):
    response = await make_get_request('/person/search/?sort=some_wrong_name')
    assert response.status == HTTPStatus.BAD_REQUEST
    assert response.body['detail'] == SORT_BY_NAME_MESSAGE


@pytest.mark.asyncio
async def test_list_only_three_people(make_get_request):
    response = await make_get_request(
        '/person/search/?page[size]=3&page[number]=1'
    )
    assert response.status == HTTPStatus.OK
    assert len(response.body) == 3
    assert response.body == PEOPLE_RESPONSE[:3]


@pytest.mark.asyncio
async def test_list_only_three_people_with_sorting(make_get_request):
    response = await make_get_request(
        '/person/search/?page[size]=3&page[number]=1&sort=-full_name'
    )
    assert response.status == HTTPStatus.OK
    assert len(response.body) == 3
    assert response.body == PEOPLE_RESPONSE_SORTED_NAME_DESC[:3]


@pytest.mark.asyncio
async def test_list_with_search(make_get_request):
    response = await make_get_request(
        f'/person/search/?query={PEOPLE_RESPONSE[0]["full_name"]}'
    )
    assert response.status == HTTPStatus.OK
    assert len(response.body) == 1
    assert PEOPLE_RESPONSE[0] in response.body


@pytest.mark.asyncio
async def test_list_with_search_with_no_result(make_get_request):
    response = await make_get_request('/person/search/?query=wrong_name')
    assert response.status == HTTPStatus.NOT_FOUND
    assert response.body['detail'] == PERSON_NOT_FOUND_MESSAGE


@pytest.mark.asyncio
async def test_fetch_exact_person_by_id(make_get_request):
    response = await make_get_request(f'/person/{PEOPLE_RESPONSE[0]["uuid"]}')
    assert response.status == HTTPStatus.OK
    assert response.body['full_name'] == PEOPLE_RESPONSE[0]['full_name']


@pytest.mark.asyncio
async def test_fetch_person_by_wrong_id(make_get_request):
    response = await make_get_request('/person/any_string')
    assert response.status == HTTPStatus.NOT_FOUND
    assert response.body['detail'] == ITEM_DOESNT_EXIST_MESSAGE


@pytest.mark.asyncio
async def test_fetch_films_by_person(make_get_request):
    response = await make_get_request(
        f'/person/{PEOPLE_RESPONSE[0]["uuid"]}/film/'
    )
    assert response.status == HTTPStatus.OK
    assert len(response.body) == 1
    assert MOVIES_RESPONSE[0] in response.body


@pytest.mark.asyncio
async def test_fetch_films_by_non_existent_person(make_get_request):
    response = await make_get_request('/person/any_string/film/')
    assert response.status == HTTPStatus.NOT_FOUND
    assert response.body['detail'] == FILMS_FOR_PERSON_NOT_FOUND_MESSAGE


@pytest.mark.asyncio
async def test_redis_stored_data(make_get_request, make_redis_request):
    await make_get_request(f'/person/{PEOPLE_RESPONSE[0]["uuid"]}')

    redis_data = await make_redis_request(PEOPLE_RESPONSE[0]['uuid'])
    item_from_redis = orjson.loads(redis_data)

    assert item_from_redis['full_name'] == PEOPLE_RESPONSE[0]['full_name']
    assert item_from_redis['uuid'] == PEOPLE_RESPONSE[0]['uuid']
