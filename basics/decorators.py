# Part 1
# Task 1.1
def cook_process(func):
    def wrapper(meal):
        print(f"Готовим {meal}")
        func(meal)
    return wrapper

@cook_process
def cook_meal(meal):
    print(f"{meal} готово")

cook_meal("суши")

# Task 1.2
def repeat(func):
    def wrapper(meal, n):
        for i in range(1, n + 1):
            print(f"{meal}: порция {i}")
        func(meal, n)

    return wrapper

@repeat
def cook_result(meal, n):
    print(f"{meal} подано")

cook_result("паста", 5)

# Task 1.3
def log_ingredients(func):
    def wrapper(meal, **ingredients):
        for key, value in ingredients.items():
            print(f"{key}: {value}")
        func(meal, **ingredients)
    return wrapper

@log_ingredients
def meal_recipe(meal, **ingredients):
    print(f"{meal} готово")

meal_recipe("Оливье", картофель = "2 шт", яйца = "3 шт", колбаса = "200 гр")

# Task 1.4
def validate_positive(func):
    def wrapper(minutes, grams_meat):
        if minutes > 0 and grams_meat > 0:
            func(minutes, grams_meat)
        else:
            print("Неверные данные")
    return wrapper

@validate_positive
def marination_rule(minutes, grams_meat):
    print(f"Мариновать {grams_meat} г мяса {minutes} мин.")

marination_rule(0, 3)
marination_rule(15, 90)

# Task 1.5
def ingredients_price(func):
    def wrapper(*prices):
        print(f"Стоимость всех ингредиентов: {sum(prices)}")
        func(*prices)
    return wrapper

@ingredients_price
def ingredient_quantity(*prices):
    print(f"Всего куплено игредиентов: {len(prices)}")

ingredient_quantity(15, 90, 345, 431, 23)

# Part 2
# Task 2.1
def filtered_list(func):
    def wrapper(films, min_rating):
        result = {}
        for key, value in films.items():
            if value >= min_rating:
                result.update({key: value})
        func(result)
    return wrapper

@filtered_list
def film_ratings(films):
    print(f"Отфильтрованные фильмы: {films}")

film_ratings({"Дюна": 9, "Матрица": 10, "Начало": 7, "Крёстный отец": 9, "Ёлки 5": 5}, 9)

# Task 2.2
def average_duration(func):
    def wrapper(duration):
        avg_duration = sum(duration.values()) / len(duration.values())
        print(f"Средняя длительность фильмов составила: {avg_duration:.2f}")
        func(duration)
    return wrapper

@average_duration
def film_duration(duration):
    print("Длительность фильмов посчитана!")

film_duration({"Дюна": 155, "Матрица": 136, "Начало": 148})

# Task 2.3
import random
def random_discount(func):
    def wrapper(*costs):
        total = sum(costs)
        discount = random.randint(10, 50)
        final = total - discount
        print(f"Скидка: {discount} руб, Итого: {final} руб")
        func(*costs)
    return wrapper

@random_discount
def count_snacks(*costs):
    quantity_snacks = len(costs)
    print(f"Количество купленных закусок: {quantity_snacks} позиции")

count_snacks(100, 400, 230)

# Task 2.4
def time_validation(func):
    def wrapper(film, time):
        if time > 8 and time < 23:
            func(film, time)
        else:
            print(f"Недопустимое время начала фильма: {time}:00")
    return wrapper

@time_validation
def current_film(film, time):
    print(f"Фильм {film} начинается в {time}:00")

current_film("Аватар", 22)
current_film("Дюна", 2)

# Task 2.5
def check_schedule(func):
    def wrapper(film, schedule):
        if film in schedule:
            func(film, schedule)
        else:
            print(f"Фильм '{film}' отсутствует в расписании")
    return wrapper

@check_schedule
def film_timetable(film, schedule):
    print(f"Фильм '{film}' начинается в {schedule[film]}")

film_timetable("Интерстеллар", {"Дюна": "18:00", "Матрица": "20:30", "Интерстеллар": "23:00", "Шрек 2": "16:20"})
film_timetable("Гарри Поттер", {"Дюна": "18:00", "Матрица": "20:30", "Интерстеллар": "23:00", "Шрек 2": "16:20"})