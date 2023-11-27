from functional.utils.populate_es_with_genres import populate_genres_to_es
from functional.utils.populate_es_with_people import populate_people_to_es
from functional.utils.populate_es_with_movies import populate_movies_to_es

if __name__ == '__main__':
    populate_genres_to_es()
    populate_people_to_es()
    populate_movies_to_es()
