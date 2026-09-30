import random
from datetime import datetime

import psycopg


def connect(**conn_params):
    try:
        conn = psycopg.connect(**conn_params)
        print("Вы успешно подключились к базе данных")
        return conn
    except psycopg.Error as e:
        print(f"Ошибка подключения к базе данных: {e}")

def close(conn):
    if conn:
        conn.close()
        print("Подключение завершено")

def trainer_info():
    trainer1 = int(input("Введите id первого тренера: "))
    trainer2 = int(input("Введите id второго тренера: "))
    return trainer1, trainer2

def get_strongest_pokemon(conn, trainer_id):
    with conn.cursor() as cursor:
        cursor.execute("""
                        SELECT
                            id,
                            name,
                            trainer_id,
                            attack
                        FROM pokemons
                        WHERE trainer_id = %s
                        ORDER BY attack DESC
                        LIMIT 1
        """, (trainer_id,))

        res = cursor.fetchone()
        if not res:
            return None

        else:
            pokemon = {
                "id": res[0],
                "name": res[1],
                "trainer_id": res[2],
                "attack": res[3]
        }
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
        else:
            loser = pokemon1

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
                                winner_attack )
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (battle_date, winner["trainer_id"], loser["trainer_id"], winner["id"], loser["id"], pokemon1["id"], loser["attack"], winner["attack"]))

            cursor.execute("""
                            UPDATE pokemons
                            SET win_count = win_count + 1
                            WHERE id = %s
                            
            """, (winner["id"],))

    return winner, loser

def print_battle_result(winner, loser):
    print(f"Покемон {winner["name"]} тренера {winner["trainer_id"]} победил в битве! Покемон {loser["name"]} тренера {loser["trainer_id"]} проиграл в битве.")

if __name__ == "__main__":
    conn_params = {
        "host": "localhost",
        "port": 5432,
        "user": "pokemonbattle_user",
        "password": "123456",
        "dbname": "pokemonbattle_db",
    }

    conn = connect(**conn_params)
    try:
        trainer1, trainer2 = trainer_info()
        pokemon1 = get_strongest_pokemon(conn, trainer1)
        pokemon2 = get_strongest_pokemon(conn, trainer2)

        conn.commit()

        if pokemon1 is None:
            print(f"У тренера {trainer1} отсутствуют покемоны. Выберите другого тренера для битвы")
        elif pokemon2 is None:
            print(f"У тренера {trainer2} отсутствуют покемоны. Выберите другого тренера для битвы")
        else:
            winner, loser = simulate_battle(conn, pokemon1, pokemon2)
            print_battle_result(winner, loser)
    finally:
        close(conn)