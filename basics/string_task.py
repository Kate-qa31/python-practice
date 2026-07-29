# Task 1.1
radius = 5
height = 10
pi = 3.14159
volume = pi * radius ** 2 * height
print(f"Радиус = {radius} см, высота = {height} см, объем цилиндра = {volume:.2f} куб. см")

# Task 1.2
temp_C = 36.6
temp_F = (temp_C * 9 / 5) + 32
print(f"Температура в градусах Цельсия: {temp_C:.1f} градусов, температура в градусах Фаренгейта: {temp_F:.2f} градусов")

# Task 1.3
distance = 185
time = 3
speed = distance / time
print(f"Скорость = {speed:.2f} км/ч, расстояние = {distance} км, время = {time} ч")

# Task 2.1
s1 = "111" * 5
print(f"s1 = {s1}")
s2 = 111 * 5
print(f"s2 = {s2}")
s3 = 111.11 * 5
print(f"s3 = {s3}")
# s4 = "111" * "111" # при умножении строки на строку получим ошибку TypeError
# print(f"s4 = {s4}")

# Task 2.2
new_str = "BOdHnKEWDpTFVgqdCkMVZTaQzXQBDjdiufEX"
if new_str.isalpha():
    print(f"Строка {new_str} содержит только буквы")
elif new_str.isdigit():
    print(f"Строка {new_str} содержит только цифры")
else:
    print(f"Строка {new_str} содержит и буквы, и цифры")

# Task 2.3
sentence = "Learning Python is fun and useful"
words = sentence.split()
print(f"В строке {sentence} {len(words)} слов")

# Task 2.4
new_string = "-".join(words)
print(f"Результат объединения слов в строку: {new_string}")

# Task 3
backpack1 = "         	пАлатка, спаЛьник, рЮКзак           	"
backpack2 = "горЕЛка!фОнарик!карта!компАС"
backpack3 = "икЧИпс"

# Task 3.1
backpack1 = backpack1.strip()
print(backpack1)

# Task 3.2
backpack2 = backpack2.split("!")
backpack2 = ", ".join(backpack2)
print(backpack2)

# Task 3.3
print(id(backpack3))
backpack3 = backpack3[::-1]
print(id(backpack3))

# Task 3.4
backpack1 = backpack1.lower()
print(backpack1)

# Task 3.5
backpack_items = backpack2[:16]
print(backpack_items)
backpack3 = backpack3 + ", " + backpack_items
print(backpack3)

# Task 3.6
backpack3 = (backpack3 + ", ")  * 2 + backpack3
print(backpack3)

# Task 3.7
print(id(backpack1))
backpack1 = backpack1 + ", " + backpack2 + ", " + backpack3
print(backpack1)
print(id(backpack1))

# Task 3.8
backpack1 = backpack1.title()
print(backpack1)

# Task 3.9
print(backpack1.find("Карта"))

# Task 3.10
length = len(backpack1)
print(f"Длина первого рюкзака составляет {length} символов")

# Task 3.11
backpack1 = backpack1.split(", ")
print(backpack1)