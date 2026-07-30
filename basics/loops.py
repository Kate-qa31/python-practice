# Task 1.1
sentence = "Python is the best programming language"
words = sentence.split()

for word in words:
    if len(word) > 3:
        print(word)
    else:
        continue

# Task 1.2
for i in range(15,101):
    if i % 13 == 0:
        print(i)
        break

# Task 1.3
for i in range (1, 31):
    if i % 5 == 0:
        continue
    else:
        print(i)

# Task 1.4
for x in range(1,101):
    for y in range(1,101):
        if x + y == 50:
            print (x,y)
            break
    if x + y == 50:
        break

# Task 1.5
for x in range(1,4):
    for y in range(1,4):
        print(f"({x},{y})", end=" ")
    print()

# Task 2
backpack = "вереВКа, спИЧки, коМПАс, нАВигатор, фОНарик, гореЛКа, рюкзАК, спалЬник, палаткА"

# Task 2.1
items = backpack.split(", ")
for item in items:
    print(item)

# Task 2.2
for index, item in enumerate(items):
    items[index] = item.capitalize()

for item in items:
    print(item)

# Task 2.3
i = 0
while i < len(items):
    items[i] = items[i][::-1]
    print(items[i])
    i += 1

# Task 2.4
vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'

for item in items:
    if item[0] in vowels:
        print(item)

# Task 2.5
i = 0
while i < len(items):
    items[i] = items[i].lower()
    print(items[i])
    i += 1

# Task 2.6
longest_word = ""
for item in items:
    if len(item) > len(longest_word):
        longest_word = item
print(f"Самое длинное слово: {longest_word}")

# Task 2.7
i = 0
while i < len(items):
    if len(items[i]) > 7:
        items.pop(i)
    else:
        i += 1
print(items)