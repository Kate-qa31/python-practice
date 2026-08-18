# Task 1
backpack = ['палатка', 'спальник', 'рюкзак', 'горелка', 'дождевик', 'фонарик', 'карта', 'компас', 'спички', 'горелка', 'телевизор', 'фонарик']

# Task 1.1
backpack[backpack.index("карта")] = "навигатор"
print(backpack)

# Task 1.2
backpack.append("верёвка")
print(backpack)

# Task 1.3
backpack.reverse()
print(backpack)
# backpack = backpack[::-1] - второй способ

# Task 1.4
backpack.remove("телевизор")
print(backpack)

# Task 1.5
middle_place = len(backpack) // 2
backpack.insert(middle_place, "бутылка")
print(backpack)

# Task 1.6
print(f"В рюкзаке {backpack.count("фонарик")} фонарика и {backpack.count("горелка")} горелки")

# Task 1.7
print(f"В рюкзаке {len(backpack)} вещей")

# Task 1.8
backpack.pop()
print(backpack)

# Task 1.9
copied_backpack = backpack.copy()
print(copied_backpack)
copied_backpack.append("вилка")
print(backpack)
print(copied_backpack)
copied_backpack.pop()

# Task 1.10
backpack2 = []
for item in backpack:
    if backpack.count(item) > 1:
        backpack.remove(item)
        backpack2.append(item)
print(f"Содержимое рюкзака 1: {backpack}, содержимое рюкзака 2: {backpack2}")

# Task 1.11
backpack.sort(reverse=True)
for item in backpack[:5]:
    backpack.remove(item)
    backpack2.append(item)
print(f"Содержимое рюкзака 1: {backpack}, содержимое рюкзака 2: {backpack2}")

# Task 2
# Содержимое рюкзака: ['фонарик', 'горелка', 'фонарик', 'спички', 'спальник', 'рюкзак', 'навигатор']
backpack = ['фонарик', 'горелка', 'фонарик', 'спички', 'спальник', 'рюкзак', 'навигатор']

# Task 2.1
length_name = [len(x) for x in backpack]
print(length_name)

# Task 2.2
backpack_things = [x for x in backpack if len(x) % 2 == 0]
print(backpack_things)

# Task 2.3
backpack_list = [f"{i}: {backpack[i]}" for i in range(0, len(backpack))]
print(backpack_list)

# Task 2.4
backpack_reversed = [i[::-1] for i in backpack]
print(backpack_reversed)

# Task 2.5
first_letter = [x[0] for x in backpack_reversed]
print(first_letter)