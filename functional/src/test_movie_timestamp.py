from http import HTTPStatus
import pytest

import json


@pytest.mark.asyncio
async def test_add_timestamp(privileged_user_session, watch_timestamp_url, movies):
    movie = movies[0]

    async with privileged_user_session.post(
            watch_timestamp_url,
            data=json.dumps({
                "film_id": movie['_id'],
                "timestamp": 100
            })) as response:
        assert response.status == HTTPStatus.OK


@pytest.mark.asyncio
async def test_add_timestamp_wrong_timestamp(privileged_user_session, watch_timestamp_url, movies):
    movie = movies[0]
    async with privileged_user_session.post(
            watch_timestamp_url,
            data=json.dumps({
                "film_id": movie['_id'],
                "timestamp": '100f'
            })) as response:
        assert response.status == HTTPStatus.UNPROCESSABLE_ENTITY


@pytest.mark.asyncio
async def test_add_timestamp_no_user(session, movies, watch_timestamp_url):
    movie = movies[0]
    async with session.post(
            watch_timestamp_url,
            data=json.dumps({
                "film_id": movie.get('_id'),
                "timestamp": 100
            })) as response:
        assert response.status == HTTPStatus.UNAUTHORIZED


@pytest.mark.asyncio
async def test_add_timestamp_wrong_id(privileged_user_session, watch_timestamp_url):
    async with privileged_user_session.post(
            watch_timestamp_url,
            data=json.dumps({
                "film_id": 'fffffff',
                "timestamp": 100
            })) as response:
        assert response.status == HTTPStatus.NOT_FOUND
