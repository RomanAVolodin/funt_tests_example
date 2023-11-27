PEOPLE = [
    {
        '_index': 'persons',
        '_id': '0387979e-8a3f-4604-bbab-8f0e8c6b02be',
        '_source': {
            'uuid': '0387979e-8a3f-4604-bbab-8f0e8c6b02be',
            'full_name': 'Harrison Ford',
            'films_directed': [],
            'films_acted': ['0a1759ef-0fbd-41ca-8669-9b379814bee4'],
            'films_written': ['0a1759ef-0fbd-41ca-8669-9b379814bee4'],
        },
    },
    {
        '_index': 'persons',
        '_id': 'fab19f2c-fa24-4691-a109-fd673c0dc5a5',
        '_source': {
            'uuid': 'fab19f2c-fa24-4691-a109-fd673c0dc5a5',
            'full_name': 'Aaron Aaronson',
            'films_directed': ['0a1759ef-0fbd-41ca-8669-9b379814bee4'],
            'films_acted': ['0a1759ef-0fbd-41ca-8669-9b379814bee4'],
            'films_written': [],
        },
    },
    {
        '_index': 'persons',
        '_id': 'f2cfd013-22b9-4245-918c-ca920a6c2c03',
        '_source': {
            'uuid': 'f2cfd013-22b9-4245-918c-ca920a6c2c03',
            'full_name': 'Irvin Kershner',
            'films_directed': [
                'eaf7a3ec-e05d-487e-9f98-787e10b74ebb',
                '0108e840-539e-4973-9475-70a901ee934e',
            ],
            'films_acted': ['ba4077a9-8e08-40b0-811a-6aad4e64a9f2'],
            'films_written': [],
        },
    },
    {
        '_index': 'persons',
        '_id': '8b593811-905f-45e4-84c0-def0926ffe63',
        '_source': {
            'uuid': '8b593811-905f-45e4-84c0-def0926ffe63',
            'full_name': 'Leigh Brackett',
            'films_directed': [],
            'films_acted': [],
            'films_written': [
                'eaf7a3ec-e05d-487e-9f98-787e10b74ebb',
                'c0f61330-76b5-4e3b-b68d-7ce4fd189ea1',
                '0108e840-539e-4973-9475-70a901ee934e',
            ],
        },
    },
    {
        '_index': 'persons',
        '_id': 'aae6c483-b25d-4547-9b99-1a07ab2d8fc4',
        '_source': {
            'uuid': 'aae6c483-b25d-4547-9b99-1a07ab2d8fc4',
            'full_name': 'Richard Marquand',
            'films_directed': ['ca6b5c42-efd0-4449-9802-f60e65273067'],
            'films_acted': [],
            'films_written': [],
        },
    },
]


MOVIES_FOR_PEOPLE = [
    {
        '_index': 'movies',
        '_id': '28f000f9-f0f0-490d-a611-b8e56357d340',
        '_source': {
            'uuid': '28f000f9-f0f0-490d-a611-b8e56357d340',
            'imdb_rating': 6.7,
            'genres_titles': 'Fantasy,Action,Adventure,Sci-Fi',
            'title': 'Star Wars: Episode V - The Empire Strikes Back',
            'is_suspicious': False,
            'description': 'Luke Skywalkern',
            'directors_names': 'Irvin Kershner',
            'actors_names': 'Billy Dee Williams,Harrison Ford,Carrie Fisher,Mark Hamill',
            'writers_names': 'George Lucas,Leigh Brackett,Lawrence Kasdan',
            'genres': [
                {
                    'uuid': 'f0f476ac-fd00-405a-a556-79faf51da130',
                    'name': 'Fantasy',
                },
                {
                    'uuid': '81f819f8-d8cd-4874-9bb2-669616c8d250',
                    'name': 'Action',
                },
                {
                    'uuid': '1e9e8dd2-69fd-4595-8667-c861e4391a23',
                    'name': 'Adventure',
                },
            ],
            'directors': [
                {
                    'uuid': '8b593811-905f-45e4-84c0-def0926ffe63',
                    'full_name': 'Leigh Brackett',
                }
            ],
            'actors': [
                {
                    'uuid': 'aae6c483-b25d-4547-9b99-1a07ab2d8fc4',
                    'full_name': 'Richard Marquand',
                },
                {
                    'uuid': 'f2cfd013-22b9-4245-918c-ca920a6c2c03',
                    'full_name': 'Irvin Kershner',
                },
            ],
            'writers': [
                {
                    'uuid': '0387979e-8a3f-4604-bbab-8f0e8c6b02be',
                    'full_name': 'Harrison Ford',
                }
            ],
        },
    },
    {
        '_index': 'movies',
        '_id': '3bf66463-0559-4f64-82fb-a927a03dfa2f',
        '_source': {
            'uuid': '3bf66463-0559-4f64-82fb-a927a03dfa2f',
            'imdb_rating': 7.5,
            'genres_titles': 'Sci-Fi,Fantasy,Adventure,Action',
            'title': 'Star Wars: Episode III - Revenge of the Sith',
            'is_suspicious': False,
            'description': 'Near the end of order.',
            'directors_names': 'George Lucas',
            'actors_names': 'Natalie Portman,Ian McDiarmid,Hayden Christensen,Ewan McGregor',
            'writers_names': 'George Lucas',
            'genres': [
                {
                    'uuid': 'be2e1a47-4b97-4c77-8e73-985a3cf3ba51',
                    'name': 'Sci-Fi',
                },
                {
                    'uuid': 'f0f476ac-fd00-405a-a556-79faf51da130',
                    'name': 'Fantasy',
                },
                {
                    'uuid': '1e9e8dd2-69fd-4595-8667-c861e4391a23',
                    'name': 'Adventure',
                },
                {
                    'uuid': '81f819f8-d8cd-4874-9bb2-669616c8d250',
                    'name': 'Action',
                },
            ],
            'directors': [
                {
                    'uuid': 'aae6c483-b25d-4547-9b99-1a07ab2d8fc4',
                    'full_name': 'George Lucas',
                }
            ],
            'actors': [
                {
                    'uuid': 'aae6c483-b25d-4547-9b99-1a07ab2d8fc4',
                    'full_name': 'Natalie Portman',
                }
            ],
            'writers': [
                {
                    'uuid': '8b593811-905f-45e4-84c0-def0926ffe63',
                    'full_name': 'George Lucas',
                }
            ],
        },
    },
]


PEOPLE_RESPONSE = [x['_source'] for x in PEOPLE]

PEOPLE_RESPONSE_SORTED_NAME_ASC = sorted(
    PEOPLE_RESPONSE, key=lambda k: k['full_name']
)

PEOPLE_RESPONSE_SORTED_NAME_DESC = sorted(
    PEOPLE_RESPONSE, key=lambda k: k['full_name'], reverse=True
)

MOVIES_RESPONSE = [
    {
        'uuid': x['_source']['uuid'],
        'title': x['_source']['title'],
        'is_suspicious': x['_source']['is_suspicious'],
        'imdb_rating': x['_source']['imdb_rating'],
    }
    for x in MOVIES_FOR_PEOPLE
]
