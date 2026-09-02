# Task 1.1
def daily_reminder():
    print("Не забудь выпить воду и сделать растяжку сегодня!")
daily_reminder()

# Task 1.2
def log_sleep(number):
    print(f"Количество часов сна сегодня: {number}")
log_sleep(8)

# Task 1.3
def calculate_water_intake(weight, age):
    if age < 30:
        water_ml = weight * 40
    elif 30 <= age <= 55:
        water_ml = weight * 35
    else:
        water_ml = weight * 30
    return water_ml / 1000
print(calculate_water_intake(60, 25))
print(calculate_water_intake(51, 32))
print(calculate_water_intake(100, 56))

# Task 1.4
def track_mood(mood="Хорошее", energy=7):
    print(f"Ваше настроение: {mood}. Уровень энергии: {energy}/10")
track_mood("Плохое", 2)
track_mood()

# Task 1.5
def list_healthy_habits(*habits):
    print("Полезные привычки: \n-", "\n- ".join(habits))
list_healthy_habits("Плавание", "Бег", "Растяжка")

# Task 1.6
def health_summary(**metrics):
    for key, value in metrics.items():
        print(f"{key}: {value}")
health_summary(sleep = "7 hours", water = "2 liters", steps = 8000, calories = 1700)

# Task 1.7
def bmi(weight: int, height: float) -> float:
    return weight / height ** 2
print(bmi(65, 1.63))

# Task 2.1
def movie_night_reminder():
    print("Не забудь устроить себе вечер кино!")
movie_night_reminder()

# Task 2.2
def print_movie_rating(movie, rating):
    print(f"Фильм {movie} получил оценку {rating}/10.")
print_movie_rating("Великий Гэтсби", 10)

# Task 2.3
def calculate_watch_time(episodes, duration):
    return episodes * duration
total_time = calculate_watch_time(5, 60)
print(f"Общее время просмотра: {total_time} минут")

# Task 2.4
def plan_movie_session(movie="Inception", snack="попкорн"):
    print(f"Фильм на сегодня: {movie}, а закуска к фильму: {snack}.")
plan_movie_session("Interstellar", "чипсы")
plan_movie_session()

# Task 2.5
def list_favorite_movies(*movies):
    print("Любимые фильмы:")
    for movie in movies:
        print(f"- {movie}")
list_favorite_movies("Начало", "Парк Юрского периода", "Волк с Уолл-стрит")

# Task 2.6
def prepare_movie_night(snack="попкорн", *movies):
    print(f"Ты выбрал закуску: {snack}")
    if movies == ():
        print("Фильмы пока не выбраны")
    else:
        print("Запланированные фильмы:")
        for movie in movies:
            print(f"- {movie}")
prepare_movie_night("сухарики", "Начало", "Парк Юрского периода", "Волк с Уолл-стрит")
prepare_movie_night()

# Task 2.7
def series_info(**infos):
    for key, value in infos.items():
        print(f"{key}: {value}")
series_info(title = "Desperate Housewives", seasons = 8, rating = 7.7, genre = "Drama, melodrama, comedy, detective")

# Task 2.8
def average_episode_duration(total_minutes:int, episodes:int) -> float:
    return total_minutes / episodes
print(f"Средняя продолжительность одной серии составляет {average_episode_duration(600, 30)} минут")

# Task 2.9
def movie_marathon_plan():
    movie_night_reminder()
    plan_movie_session("Avatar", "пицца")
movie_marathon_plan()