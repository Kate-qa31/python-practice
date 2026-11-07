from http import HTTPStatus

import pytest
import requests

BASE_URL = "https://api.pokemonbattle.ru/v2"
TOKEN = {"trainer_token": POKEMON_TRAINER_TOKEN}
trainers_pokemon_payload = {
            "trainer_id": 242,
            "status": 1
        }

@pytest.fixture(scope="session")
def api_session():
    with requests.Session() as pokemon_session:
        yield pokemon_session


class TestGetTrainers:
    def test__trainers__get_city(self, api_session):
        payload = {"city": "Samara"}
        response = api_session.get(
            BASE_URL + "/trainers",
            params=payload
        )
        assert response.status_code == 200
        body = response.json()
        assert isinstance(body["data"], list)
        for trainer in body["data"]:
            assert trainer["city"] == "Samara"

    def test__trainers__get_id(self, api_session):
        payload = {"trainer_id": 242}
        response = api_session.get(
            BASE_URL + "/trainers",
            params=payload
        )
        assert response.status_code == 200
        body = response.json()
        assert isinstance(body["data"], list)
        assert len(body["data"]) == 1
        assert body["data"][0]["id"] == "242"

    def test__trainers__get_city_sorted_desc_level(self, api_session):
        payload = {
            "city": "Москва",
            "sort": "desc_level"
        }
        response = api_session.get(
            BASE_URL + "/trainers",
            params=payload
        )
        assert response.status_code == 200
        body = response.json()
        assert isinstance(body["data"], list)
        assert len(body["data"]) >= 2
        for trainer in body["data"]:
            assert trainer["city"] == "Москва"
        for i in range(len(body["data"]) - 1):
            assert int(body["data"][i]["level"]) >= int(body["data"][i+1]["level"])

class TestChangeNamePokemon:
    def get_alive_pokemons(self, api_session):
        response_pokemons_list = api_session.get(
            BASE_URL + "/pokemons",
            params=trainers_pokemon_payload
        )
        pokemons_alive_list = response_pokemons_list.json()
        pokemon_id_info = []

        for pokemon in pokemons_alive_list.get("data", []):
            pokemon_id_info.append(pokemon["id"])
        return pokemon_id_info

    def knockout_pokemon(self, api_session):
        pokemon_id_info = self.get_alive_pokemons(api_session)

        for pokemon_id in pokemon_id_info:
            knockout_response = api_session.post(
                BASE_URL + "/pokemons/knockout",
                json={"pokemon_id": pokemon_id},
                headers=TOKEN
            )
            assert knockout_response.status_code == 200

    def check_alive_pokemons(self, api_session):

        alive_check = api_session.get(
            BASE_URL + "/pokemons",
            params={"trainer_id": 242},
        )
        assert alive_check.status_code == 200
        body = alive_check.json()
        for pokemon in body["data"]:
            assert pokemon["status"] == 0

    def create_pokemon(self, api_session):
        created_pokemon_id = api_session.post(
            BASE_URL + "/pokemons",
            headers=TOKEN,
            json={
                "name": "Cookie",
                "photo_id": 3
            }
        )
        assert created_pokemon_id.status_code == 201
        pokemon_id = created_pokemon_id.json()["id"]
        return pokemon_id

    def test__pokemon__change_name(self, api_session):
        self.knockout_pokemon(api_session)
        self.check_alive_pokemons(api_session)
        created_pokemon_id = self.create_pokemon(api_session)
        changed_pokemon = api_session.patch(
            BASE_URL + "/pokemons",
            headers=TOKEN,
            json={
                "pokemon_id": created_pokemon_id,
                "name": "Pikachu"
            }
        )
        assert changed_pokemon.status_code == 200

        get_name_pokemon = api_session.get(
            BASE_URL + "/pokemons",
            params={"pokemon_id": created_pokemon_id}
        )
        assert get_name_pokemon.status_code == 200
        pokemon_name = get_name_pokemon.json()["data"][0]["name"]
        assert pokemon_name == "Pikachu"


