# Task 1
europe_set = {"Франция", "Сербия", "Андорра", "Норвегия", "Португалия", "Бельгия"}
asia_set = {"Япония", "Лаос", "Шри-Ланка", "Китай", "Филиппины", "Камбоджа"}

# Task 1.1
europe_set.add("Исландия")
print(europe_set)

# Task 1.2
asia_set.discard("Япония")
print(asia_set)
asia_set.discard("Вьетнам") # ошибки не будет, даже если элемента нет
print(asia_set)
# asia_set.remove("Вьетнам") # вызовет KeyError, если элемента нет

# Task 1.3
new_europe_countries = {"Испания", "Греция", "Норвегия"}
europe_set.update(new_europe_countries)
print(europe_set)

# Task 1.4
deleted_country = europe_set.pop()
print(deleted_country)

# Task 1.5
my_dream_countries = set()
my_dream_countries.add("Испания")
my_dream_countries.add("Турция")
my_dream_countries.add("Египет")
my_dream_countries.add("Монако")
my_dream_countries.add("Тунис")
print(my_dream_countries)

# Task 1.6
my_dream_countries.clear()
print(my_dream_countries)

# Task 2
visited = {"Италия", "Франция"}

wishlist = {"Франция", "Япония", "Норвегия"}


european_cities = {"Париж", "Берлин"}

asian_cities = {"Токио", "Сеул"}


eco = {"Грузия", "Норвегия"}

cheap = {"Грузия", "Армения"}


summer = {"Италия", "Испания"}

winter = {"Норвегия"}


not_interested = {"Вьетнам", "Гренландия"}

invited_by_friends = {"Гренландия", "Исландия"}

# Task 2.1
print(wishlist - visited)

# Task 2.2
print(visited & wishlist)

# Task 2.3
print(european_cities | asian_cities)

# Task 2.4
print(eco.symmetric_difference(cheap))

# Task 2.5
if winter.issubset(wishlist):
    print("Страны с развитым зимним туризмом входят в список желаемых стран")
else:
    print("Страны с развитым зимним туризмом не входят в список желаемых стран")

# Task 2.6
print(summer.union(winter))

# Task 2.7
if "Сеул" in asian_cities:
    print("Сеул входит в множество азиатских городов")
else:
    print("Сеул не входит в множество азиатских городов")

# Task 2.8
print(eco.intersection(cheap))

# Task 2.9
print(invited_by_friends.difference(not_interested))

# Task 2.10
if invited_by_friends.issuperset(winter):
    print("В страны, куда зовут друзья, входят страны с развитым зимним туризмом")
else:
    print("В страны, куда зовут друзья, не входят страны с развитым зимним туризмом")