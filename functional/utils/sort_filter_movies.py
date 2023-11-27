def sort_movies_by_imdb_rating(movies, desc=True):
    return sorted(movies, key=lambda k: k['imdb_rating'], reverse=desc)


def filter_non_suspicious_movies(movies):
    return list(filter(lambda x: x['is_suspicious'] is not True, movies))


def filter_suspicious_movies(movies):
    return list(filter(lambda x: x['is_suspicious'] is True, movies))
