import asyncio
import os
from dataclasses import dataclass

import aiohttp
import aioredis
import pytest
from elasticsearch import AsyncElasticsearch
from multidict import CIMultiDictProxy

from functional.testdata.test_users import (
    PASSWORD,
    PRIVILEGED_USER_EMAIL,
    ADMIN_USER_EMAIL,
)

SERVICE_URL = 'http://{}:{}'.format(
    os.getenv('FAST_API_HOST'), os.getenv('FAST_API_PORT')
)
AUTH_URL = 'http://{}:{}'.format(
    os.getenv('AUTH_HOST'), os.getenv('AUTH_PORT')
)


@dataclass
class HTTPResponse:
    body: dict
    headers: CIMultiDictProxy[str]
    status: int


@pytest.fixture
def api_url():
    return f'{SERVICE_URL}/api/v1'


@pytest.fixture
def watch_timestamp_url(api_url):
    method = '/film/watch_timestamp/'
    url = api_url + method
    return url


@pytest.fixture(scope='session')
async def es_client():
    es_hosts = '{}:{}'.format(
        os.getenv('ELASTIC_HOST'), os.getenv('ELASTIC_PORT')
    )
    client = AsyncElasticsearch(hosts=es_hosts)
    yield client
    await client.close()


@pytest.fixture(scope='session')
async def session():
    session = aiohttp.ClientSession()
    yield session
    await session.close()


@pytest.fixture(scope='session')
async def privileged_user_session(session):
    data = {'email': PRIVILEGED_USER_EMAIL, 'password': PASSWORD}
    async with session.post(AUTH_URL + '/v1/login', json=data) as response:
        body = await response.json()
        token = body['access']
        headers = {'Authorization': f'Bearer {token}'}
        session = aiohttp.ClientSession(headers=headers)
        yield session
        await session.close()


@pytest.fixture(scope='session')
async def admin_user_session(session):
    data = {'email': ADMIN_USER_EMAIL, 'password': PASSWORD}
    async with session.post(AUTH_URL + '/v1/login', json=data) as response:
        body = await response.json()
        token = body['access']
        headers = {'Authorization': f'Bearer {token}'}
        session = aiohttp.ClientSession(headers=headers)
        yield session
        await session.close()


@pytest.fixture
def make_get_request(session, privileged_user_session, admin_user_session):
    async def inner(
        method: str, params: dict = None, user_role: str = 'user'
    ) -> HTTPResponse:
        params = params or {}
        url = SERVICE_URL + '/api/v1' + method
        inner_session = session
        if user_role == 'privileged_user':
            inner_session = privileged_user_session
        if user_role == 'admin':
            inner_session = admin_user_session
        async with inner_session.get(url, params=params) as response:
            return HTTPResponse(
                body=await response.json(),
                headers=response.headers,
                status=response.status,
            )

    return inner


@pytest.fixture(scope='session')
async def redis_session():
    redis = await aioredis.create_redis_pool(
        (os.getenv('REDIS_HOST'), os.getenv('REDIS_PORT')),
        minsize=10,
        maxsize=20,
    )
    yield redis
    redis.close()


@pytest.fixture
def make_redis_request(redis_session):
    async def inner(key: str):
        with await redis_session as redis:
            return await redis.get(key)

    return inner


@pytest.fixture(scope='session')
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
