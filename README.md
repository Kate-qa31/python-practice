# Python Practice 🐍

A repository for learning Python and developing practical QA automation skills.

## About

This project contains my Python exercises and practical assignments as I work towards API and UI test automation.

## Project Structure

- `basics/` — Python fundamentals and practice exercises.
- `oop/` — Object-oriented programming.
- `database/` — PostgreSQL and database interaction.
- `pokemonbattle_api_tests/` — API tests for the PokemonBattle application using pytest and requests.

## Tech Stack

- Python 3
- pytest
- requests
- PostgreSQL
- psycopg

## API Testing

The `pokemonbattle_api_tests` directory includes automated tests for:

- Retrieving trainers using query parameters.
- Filtering and sorting trainers.
- Creating a Pokémon.
- Sending existing Pokémon into knockout.
- Updating a Pokémon's name using PATCH.
- Verifying the updated data using GET.

## Installation

Install the project dependencies:

```bash
pip install -r requirements.txt
```

## Running Tests

Run the API tests with:

```bash
python -m pytest pokemonbattle_api_tests/ -v
```

API tests requiring authentication use the `POKEMON_TRAINER_TOKEN` environment variable. Set it before running the tests.

## Current Focus

Improving Python skills and learning to build maintainable automated API tests.