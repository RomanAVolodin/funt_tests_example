import os

from elasticsearch import Elasticsearch, helpers

from functional.testdata.movies import MOVIES
from .logger import logger

es = Elasticsearch(hosts=[os.getenv('ELASTIC_HOST')])


def populate_movies_to_es():
    logger.info('Populating movies index with test data...')
    helpers.bulk(es, MOVIES)
