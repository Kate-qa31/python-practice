import pytest
import requests


@pytest.fixture(scope="session")
def api_session():
    with requests.Session() as pokemon_session:
        yield pokemon_session