import os

from elasticsearch import Elasticsearch, helpers

from functional.testdata.people import PEOPLE, MOVIES_FOR_PEOPLE
from .logger import logger

es = Elasticsearch(hosts=[os.getenv('ELASTIC_HOST')])


def populate_people_to_es():
    logger.info('Populating People index with test data...')
    helpers.bulk(es, PEOPLE)
    helpers.bulk(es, MOVIES_FOR_PEOPLE)
