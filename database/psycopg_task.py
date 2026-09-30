import random
import sys
from datetime import datetime


import psycopg

def connect(conn_params):
    try:
        conn = psycopg.connect(**conn_params)
        print("Успешное подключение к базе данных")
        return conn
    except psycopg.Error as e:
        print(f"Ошибка подключения: {e}", file=sys.stderr)
        return None

def close(conn):
    if conn:
        conn.close()
        print("Подключение завершено")

def get_strongest_pokemon(conn, trainer_id):
        with conn.cursor() as cursor:
            cursor.execute("""
                            SELECT
                                id,
                                name,
                                attack,
                                trainer_id
                            FROM pokemons
                            WHERE trainer_id = %s
                            ORDER BY attack DESC
                            LIMIT 1
                        """, (trainer_id,))

            res = cursor.fetchone()

            if not res:
                return None

            pokemon = {
                "id" : res[0],
                "name" : res[1],
                "attack" : res[2],
                "trainer_id" : res[3]}

            return pokemon

def simulate_battle(conn, pokemon1, pokemon2):
    if pokemon1["attack"] > pokemon2["attack"]:
        winner = pokemon1
        loser = pokemon2
    elif pokemon2["attack"] > pokemon1["attack"]:
        winner = pokemon2
        loser = pokemon1
    else:
        winner = random.choice([pokemon1, pokemon2])
        if winner == pokemon1:
            loser = pokemon2
        else: loser = pokemon1

    battle_date = datetime.now()

    with conn.transaction():
        with conn.cursor() as cursor:
            cursor.execute("""
                            INSERT INTO battles (
                                date,
                                trainer_winner_id,
                                trainer_loser_id,
                                winner,
                                loser,
                                attacking_pok_id,
                                loser_attack,
                                winner_attack
                            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (battle_date, winner["trainer_id"], loser["trainer_id"], winner["id"], loser["id"], pokemon1["id"], loser["attack"], winner["attack"]))

            cursor.execute("""
                            UPDATE pokemons
                            SET win_count = win_count + 1
                            WHERE id = %s
            """, (winner["id"],))

    return winner, loser


if __name__ == "__main__":
    conn_params = {
        "dbname": "pokemonbattle_db",
        "user": "pokemonbattle_user",
        "password": "123456",
        "host": "localhost",
        "port": 5432,
    }

    conn = connect(conn_params)

    if conn is not None:
        try:
        #      trainer_id = 9903
        #     pokemon = get_strongest_pokemon(conn, trainer_id)
        #     print(f"\nСамый сильный покемон тренера {trainer_id}: {pokemon}")
            pokemon1 = {
                "id" : 84,
                "name" : "solgaleo",
                "attack" : 6,
                "trainer_id" : 112}
            pokemon2 = {
                "id" : 83,
                "name" : "mantine",
                "attack" : 7,
                "trainer_id" : 81}
            winner, loser = simulate_battle(conn, pokemon1, pokemon2)
            print(f"Покемон {winner["name"]} победил!. Покемон {loser["name"]} проиграл!")
        finally:
            close(conn)


