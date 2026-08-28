# Task 1
trip = {
"tourist":{"name":"Anna", "lastname":"Moreau", "country":"France", "age":32},
"plan":{"Italy":"Rome", "France":"Paris", "Germany":"Berlin", "Ireland":"Dublin"},
"costs":{"flight":330, "hotel":650, "meals":100, "museums":120}
}

# Task 1.1
for key in trip["tourist"]:
    if len(key) > 4:
        print(key)

# Task 1.2
suitable_pairs = {key: value for key, value in trip["tourist"].items() if isinstance(value, str) and len(value) > 5}
print(suitable_pairs)

# Task 1.3
for i, (key, value) in enumerate(trip["plan"].items()):
    print(f"{i+1}. Страна: {key}, город: {value}")

# Task 1.4
count = 0
for value in trip["plan"].values():
    if len(value) < 6:
        count = count + 1
print(f" В словаре plan {count} значений короче 6 символов")

# Task 1.5
for key, value in trip["plan"].items():
    if value == "Rome":
        print(key)

# Task 1.1
print([key for key in trip["plan"].keys() if key[0] == "F" or key[0] == "G"])

# Task 1.2
print(dict(sorted(trip["tourist"].items())))

# Task 1.3
for value in trip["plan"].values():
    if "e" in value:
        print(value)

# Task 1.4
total = 0
for value in trip["costs"].values():
    if value > 100:
        total = total + value
print(total)

# Task 1.5
result = []
for key, value in trip["plan"].items():
    if key[0] == "I" or "a" in value:
        result.append(f"{key} -> {value}")
print(result)

# Task 2.1
trip["tourist"].setdefault("email", "anna.moreau@example.com")
print(trip["tourist"])

# Task 2.2
trip["tourist"]["age"] += 1
print(trip["tourist"])

# Task 2.3
trip["costs"].update({"transport": 60})
print(trip["costs"])

# Task 2.4
attraction = trip["costs"].pop("museums")
print(attraction)

# Task 2.5
trip["tourist"].clear()
print(bool(trip["tourist"]))

# Task 2.6
backup_costs = trip["costs"].copy()
backup_costs["hotel"] = 500
print(trip["costs"])
print(backup_costs)

# Task 2.7
trip["tourist"].setdefault("phone", "+7-123-456-7890")
print(trip["tourist"])

# Task 2.8
trip["costs"].update(
    {
        key: round(value * 1.1, 1)
        for key, value in trip["costs"].items()
    }
)
print(trip["costs"])

# Task 2.9
trip_shallow = trip.copy()
import copy
trip_deep = copy.deepcopy(trip)
trip_shallow["costs"]["hotel"] = 700
trip_deep["costs"]["flight"] = 290
print(trip["costs"])
print(trip_shallow["costs"])
print(trip_deep["costs"])

# Task 2.10
new_trip = {"Spain": "Barcelona"}
trip["plan"].update(new_trip)
print(trip["plan"])

# Task 2.11
trip["plan"].popitem()
print(trip["plan"])

# Task 2.12
trip["plan"].pop("France")
print(trip["plan"])

# Task 2.13
trip["plan"] = {key: value for key, value in trip["plan"].items() if value[0] == "D"}
print(trip["plan"])

# Task 2.14
trip["plan"] = {value: key for key, value in trip["plan"].items()}
print(trip["plan"])

# Task 3
cities = {'Paris': 250, 'Berlin': 180, 'Rome': 200, 'Madrid': 170, 'Vienna': 190}

# Task 3.1
discount_prices  = {key: round(value * 0.9, 2) for key, value in cities.items()}
print(discount_prices)

# Task 3.2
cheap_prices = {key: value for key, value in cities.items() if value < 200}
print(cheap_prices)

# Task 3.3
low_items = {key.lower(): value for key, value in cities.items()}
print(low_items)

# Task 3.4
changed_cities = {length: [city for city in cities if len(city) == length] for length in [len(c) for c in cities]}
print(changed_cities)

# Task 3.5
with_sorted_price = {city: "Дорого" if price > 200 else "Приемлемо" for city, price in cities.items()}
print(with_sorted_price)