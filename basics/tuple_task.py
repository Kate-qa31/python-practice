# Task 1
cities = ("Париж", "Рим", "Берлин", "Лондон", "Москва")
landmarks = ("Лувр", "Колизей", "Бундестаг", "Биг Бен", "Кремль")

# Task 1.1
for i, city in enumerate(cities):
    print(f"{i+1}. {city}")

# Task 1.2
for i in range(len(cities)):
    print(f"{i + 1}. {cities[i]}")

# Task 1.3
cities_reversed = cities[::-1]
print(cities_reversed)

# Task 1.4
print(cities[1:len(cities)-1])

# Task 1.5
print(cities[1::2])

# Task 1.6
for place in landmarks:
    if place[0] == "Б":
        print(place)

# Task 1.7
first_city_index = cities.index("Берлин")
last_city_index = first_city_index + 3
print(cities[first_city_index:last_city_index])

# Task 1.8
double_cities = cities[:]*2
print(double_cities)

# Task 1.9
for city in cities[:3]:
    print(city + "!")

# Task 1.10
print("ID кортежа:", id(cities))
added_cities = ("Оренбург", "Самара")
cities = cities + added_cities
print(cities)
print("ID кортежа после изменения:", id(cities))

# Task 2
visited = ("Рим", "Париж", "Рим", "Вена", "Париж", "Рим")
countries = ("Франция", "Италия", "Франция", "Австрия", "Германия", "Германия")
eurotrip = ("Минск", "Варшава", "Будапешт", ["Загреб", "Зальцбург", "Вена"], "Мюнхен")

# Task 2.1
visited_set = set(visited)
for city in visited_set:
    amount = visited.count(city)
    print(f"{city}: {amount} раз(а)")

# Task 2.2
print(visited.index("Вена"))

# Task 2.3
if "Амстердам" in visited:
    print("Турист был в Амстердаме")
else:
    print("Турист не был в Амстердаме")

# Task 2.4
k = 0
max_city = ""
for city in visited:
    amount = visited.count(city)
    if amount > k:
        k = amount
        max_city = city
print(max_city)

# Task 2.5
for city in visited:
    if visited.count(city) == 1:
        print(city)

# Task 2.6
set_countries = set(countries)
print(f"Количество уникальных стран: {len(set_countries)}")

# Task 2.7
for index, city in enumerate(visited):
    if city == "Париж":
        print(index)

# Task 2.8
rome_visits = visited.count("Рим")
vienna_visits = visited.count("Вена")
if rome_visits > vienna_visits:
    print("У Рима больше посещений, чем у Вены")
else:
    print("У Вены больше посещений, чем у Рима")

# Task 2.9
set_visited = set(visited)
for city in set_visited:
    amount = visited.count(city)
    if amount > 1:
        print(city, amount)

# Task 2.10
print(visited.index("Вена", 2, 5))

# Task 2.11
print(f"Содержимое кортежа eurotrip: {eurotrip}, ID: {id(eurotrip)}")
eurotrip[3].append("Любляна")
eurotrip[3].remove("Зальцбург")
print(f"Содержимое кортежа eurotrip после изменения списка: {eurotrip}, ID: {id(eurotrip)}")