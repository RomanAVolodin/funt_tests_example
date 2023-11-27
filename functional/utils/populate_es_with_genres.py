import os

from elasticsearch import Elasticsearch, helpers

from functional.testdata.genres import GENRES
from .logger import logger

es = Elasticsearch(hosts=[os.getenv('ELASTIC_HOST')])


def populate_genres_to_es():
    logger.info('Populating Genre index with test data...')
    helpers.bulk(es, GENRES)
