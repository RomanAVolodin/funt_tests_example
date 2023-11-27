import pytest

from functional.testdata.people import PEOPLE


@pytest.fixture
def people():
    return PEOPLE
