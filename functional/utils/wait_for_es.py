import os

from elasticsearch import Elasticsearch

from backoff import backoff
from logger import logger


es = Elasticsearch(hosts=[os.getenv('ELASTIC_HOST')])


@backoff(logger=logger)
def try_elastic():
    if not es.ping():
        raise Exception('ES is not ready yet...')


if __name__ == '__main__':
    try_elastic()
    logger.info('ES is ready, continue...')
