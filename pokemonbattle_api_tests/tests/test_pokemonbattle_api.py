import requests
import pytest

from pokemonbattle_api_tests.config.api_config import BASE_URL
from pokemonbattle_api_tests.config.api_config import TOKEN

from pokemonbattle_api_tests.data.api_constants import TRAINER_ID
from pokemonbattle_api_tests.data.api_constants import CITY
from pokemonbattle_api_tests.data.api_constants import POKEMON_ORIGIN_NAME
from pokemonbattle_api_tests.data.api_constants import POKEMON_CHANGED_NAME
trainers_pokemon_payload = {
            "trainer_id": TRAINER_ID,
            "status": 1
        }


class TestGetTrainers:
    @pytest.mark.smoke
    def test__trainers__get_city(self, api_session):
        payload = {"city": CITY}
        response = api_session.get(
            BASE_URL + "/trainers",
            params=payload
        )
        assert response.status_code == 200
        body = response.json()
        assert isinstance(body["data"], list)
        for trainer in body["data"]:
            assert trainer["city"] == CITY

    @pytest.mark.smoke
    def test__trainers__get_id(self, api_session):
        payload = {"trainer_id": TRAINER_ID}
        response = api_session.get(
            BASE_URL + "/trainers",
            params=payload
        )
        assert response.status_code == 200
        body = response.json()
        assert isinstance(body["data"], list)
        assert len(body["data"]) == 1
        assert body["data"][0]["id"] == "242"

    @pytest.mark.regress
    def test__trainers__get_city_sorted_desc_level(self, api_session):
        payload = {
            "city": CITY,
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
            assert trainer["city"] == CITY
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
            params={"trainer_id": TRAINER_ID},
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
                "name": POKEMON_ORIGIN_NAME,
                "photo_id": 6
            }
        )
        assert created_pokemon_id.status_code == 201
        pokemon_id = created_pokemon_id.json()["id"]
        return pokemon_id

    @pytest.mark.skip("Known bug")
    @pytest.mark.regress
    def test__pokemon__change_name(self, api_session):
        self.knockout_pokemon(api_session)
        self.check_alive_pokemons(api_session)
        created_pokemon_id = self.create_pokemon(api_session)
        changed_pokemon = api_session.patch(
            BASE_URL + "/pokemons",
            headers=TOKEN,
            json={
                "pokemon_id": created_pokemon_id,
                "name": POKEMON_CHANGED_NAME
            }
        )
        assert changed_pokemon.status_code == 200

        get_name_pokemon = api_session.get(
            BASE_URL + "/pokemons",
            params={"pokemon_id": created_pokemon_id}
        )
        assert get_name_pokemon.status_code == 200
        pokemon_name = get_name_pokemon.json()["data"][0]["name"]
        assert pokemon_name == POKEMON_CHANGED_NAME


