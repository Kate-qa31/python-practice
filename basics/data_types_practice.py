# Task 1
user = ("Anna", "Ivanova", 28, "QA Engineer", "Moscow", "anna@test.com")
# Task 1.1
first_name, last_name, *info = user
# Task 1.2
print(user[2:5])
# Task 1.3
print(f"{first_name} {last_name}, {user[2]} лет")
# Task 1.4
k = user.count("Moscow")
print(f"Строка 'Moscow' встречается в кортеже {k} раз")

# Task 2
visits = ["anna", "ivan", "max", "anna", "kate", "ivan", "anna", "max"]
set_visits = set(visits)
unique_visits = list(set_visits)
print(unique_visits)

quantity_of_visits = len(set_visits)
print(quantity_of_visits)

print("max" in set_visits)

# Task 3
book = {
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "year": 1937,
    "genre": "Fantasy",
    "available_copies": 4,
}
# Task 3.1
print(book.get("price")) # ключ не существует, безопасный доступ к элементу, ошибка отсутствует

# Task 3.2
for key, value in book.items():
    print (f"{key}: {value}")

# Task 3.3
for key in book:
    print(key)

for value in book.values():
    print(value)

# Task 3.4
for i, (key, value) in enumerate(book.items(), start=1):
    print(f"{i}. {key}: {value}")