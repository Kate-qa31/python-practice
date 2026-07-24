# Task 1
total = int(input("Введите сумму: "))
if total >= 5000:
    discount = 0.2
    print(f"Ваша скидка: {discount}")
elif total >= 3000:
    discount = 0.1
    print(f"Ваша скидка: {discount}")
elif total >= 1000:
    discount = 0.05
    print(f"Ваша скидка: {discount}")
else:
    discount = 0
final = total * (1 - discount)
print(f"Итого: {final} руб.")

# Task 2
password = input("Введите пароль: ")
forbidden_passwords = {"password", "12345678"}
if len(password) >= 8 and password not in forbidden_passwords:
    print("Пароль принят")
else:
    print("Слабый пароль")

# Task 3
n = input("Введите число: ")
if n.isdigit() or (n.startswith("-") and n[1:].isdigit()):
    n = int(n)
    if n % 2 == 0 and n > 0:
        print(f"Число n = {n}. Оно чётное положительное")
    elif n % 2 == 0 and n < 0:
        print(f"Число n = {n}. Оно чётное отрицательное")
    elif n == 0:
        print(f"Число n = {n}. Оно ноль")
    else:
        print(f"Число n = {n}. Оно нечётное")
else:
    print("Ошибка! Нужно ввести число")