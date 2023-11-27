GENRES = [
    {
        '_index': 'genres',
        '_id': 'fe2fad59-8106-407a-9877-edb4a00350b5',
        '_source': {
            'uuid': 'fe2fad59-8106-407a-9877-edb4a00350b5',
            'name': 'Action',
        },
    },
    {
        '_index': 'genres',
        '_id': '6116193b-af1d-44ce-aadf-565b301ff7fd',
        '_source': {
            'uuid': '6116193b-af1d-44ce-aadf-565b301ff7fd',
            'name': 'Adventure',
        },
    },
    {
        '_index': 'genres',
        '_id': 'cecd0730-c7e4-409e-abf6-43b2780d45ff',
        '_source': {
            'uuid': 'cecd0730-c7e4-409e-abf6-43b2780d45ff',
            'name': 'Fantasy',
        },
    },
    {
        '_index': 'genres',
        '_id': '4120e21d-1c7e-43bd-ba72-c81057f4b0d1',
        '_source': {
            'uuid': '4120e21d-1c7e-43bd-ba72-c81057f4b0d1',
            'name': 'Sci-Fi',
        },
    },
    {
        '_index': 'genres',
        '_id': '85aa5362-666c-4ec9-8f1f-16901246a676',
        '_source': {
            'uuid': '85aa5362-666c-4ec9-8f1f-16901246a676',
            'name': 'Drama',
        },
    },
    {
        '_index': 'genres',
        '_id': 'ee3f8298-49b2-45a6-a7d8-2d86dfcf93a7',
        '_source': {
            'uuid': 'ee3f8298-49b2-45a6-a7d8-2d86dfcf93a7',
            'name': 'Music',
        },
    },
    {
        '_index': 'genres',
        '_id': 'd21ca942-9a82-4108-a3a4-9901ee60c9b6',
        '_source': {
            'uuid': 'd21ca942-9a82-4108-a3a4-9901ee60c9b6',
            'name': 'Romance',
        },
    },
    {
        '_index': 'genres',
        '_id': 'b085ca91-d314-4a2c-b1a0-5724b3ba3bc9',
        '_source': {
            'uuid': 'b085ca91-d314-4a2c-b1a0-5724b3ba3bc9',
            'name': 'Thriller',
        },
    },
    {
        '_index': 'genres',
        '_id': '229afe3f-3967-4f08-962d-1e578dccd738',
        '_source': {
            'uuid': '229afe3f-3967-4f08-962d-1e578dccd738',
            'name': 'Mystery',
        },
    },
    {
        '_index': 'genres',
        '_id': '17628cc7-48cb-492a-825f-dc35bafe4ecb',
        '_source': {
            'uuid': '17628cc7-48cb-492a-825f-dc35bafe4ecb',
            'name': 'Comedy',
        },
    },
]


GENRES_RESPONSE = [x['_source'] for x in GENRES]

GENRES_RESPONSE_SORTED_NAME_ASC = sorted(
    GENRES_RESPONSE, key=lambda k: k['name']
)
GENRES_RESPONSE_SORTED_NAME_DESC = sorted(
    GENRES_RESPONSE, key=lambda k: k['name'], reverse=True
)
