# Task 1
a = [4, 5, 6]
b = [4, 5, 6]

print(a == b)
print(a is b)

a = 15
b = 15

print(a != b)
print(a is b)

a = "Python"
b = "Python"

print(a == b)
print(a is b)

a = 200
b = 150
b += 50

print(a == b)
print(a is b)

a = 300
b = 250
b += 50

print(a == b)
print(a is b)

a = ["10", "20", "30", "40"]
b = "20"
c = 30

print(b in a)
print(not(c not in a))

# Task 2
x = 10

print(x > 8 and x > 25)
print(x > 8 and x < 25)
print(x < 8 and x < 25)
print(x < 8 and x > 25)

print(x > 8 or x > 25)
print(x > 8 or x < 25)
print(x < 8 or x < 25)
print(x < 8 or x > 25)

print(not (x < 8 and x < 25))
print(not (x > 8 or x < 25))

x = 4

print(x >= 4 and x > 16)
print(x > 4 and x < 16)
print(x <= 4 and x < 16)
print(x < 4 and x > 16)

print(x >= 4 or x > 16)
print(x > 4 or x < 16)
print(x < 4 or x < 16)
print(x <= 4 or x > 16)

print(not(x > 4 and x < 16))
print(not(x <= 4 or x < 16))

a = "hello"
b = ""

print(a and b)
print(a or b)

a = [1, 2, 3]
b = [4, 5, 6]

print(a and b)
print(a or b)

# Task 3
a = True
b = False
print(a and b or not a and not b)
print(not (a or b) and (a or not b))
print((a and not b) or (b and not a))

# Task 4
x = 5
y = 10
print(y > x * x or y >= 2 * x and x < y)

x = 3
y = 7
print(not (x * 2 == y or y - x < 2))

x = 4
y = 2
print(x > y and y != 0 or x / y > 3)

# Task 5
x = 6
print(x >= 9 and x < 18)

x = 80
print(x < 23 or x > 60)

# Task 6
x = 10
y = 7
print((x is not  None and y is not None) and (x > 0 or y > 0))
print(x % 2 == 0  and x % 4 != 0)