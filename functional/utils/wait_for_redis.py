import os
from time import sleep

from redis import Redis

from backoff import backoff
from logger import logger

redis_pool = Redis(os.getenv('REDIS_HOST'))


@backoff(logger=logger)
def try_redis():
    redis_pool.ping()


if __name__ == '__main__':
    try_redis()
    logger.info('Redis is ready, continue...')
