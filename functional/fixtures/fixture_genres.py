import pytest

from functional.testdata.genres import GENRES


@pytest.fixture
def genres():
    return GENRES
