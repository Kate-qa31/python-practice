# Task 1.1
# Program 1
number = int(input("Введите число: "))

if number < 0:
    print("Отрицательное")
else:
    print("Положительное или ноль")

# Program 2
number = int(input("Введите число: "))

if number % 2 == 0:
    print("Чётное")
else:
    print("Нечётное")

# Program 3
number = int(input("Введите число: "))

if number > 100:
    print("Число слишком большое")
else:
    print("Число подходит")

# Task 1.2
number = int(input("Введите число: "))
if number >= 9 and number < 18:
    print("Вы записаны!")
else:
    print("Ошибка! Вы выбрали нерабочее время")

# Task 2.1
number = int(input("Введите число: "))

if -100 <= number < 0:
    print("Отрицательное")
elif number == 0:
    print("Ноль")
elif 0 < number <= 100:
    print("Положительное")
else:
    print("Ошибка")

# Task 2.2
age = int(input("Введите возраст: "))
if age <= 0:
    print("Ошибка")
elif age < 23:
    print("Ваша студенческая скидка 20%")
elif age > 60:
    print("Ваша пенсионная скидка 30%")
else:
    print("Скидка не предусмотрена")

# Task 2.3
milk_list_available = ["burenka", "prostokvashino", "vkusnoteevo", "happy cow"]
milk_list_not_available = ["domik v derevne", "nasha korova"]

milk_name = input("Введите название молока: ").lower()

if milk_name in milk_list_available:
    print("Заказ принят!")
elif milk_name in milk_list_not_available:
    print("К сожалению, данный продукт закончился")
else:
    print("Мы не продаем данную продукцию")

# Task 2.4
age = input("Введите возраст: ")

if not age.isdigit() or int(age) == 0:
    print("Ошибка")
else:
    age = int(age)
    if age < 18:
        print("Несовершеннолетний")
    elif 18 <= age <= 59:
        print("Взрослый")
    else:
        print("Пенсионер")

# Task 3.1
password = input("Придумайте пароль: ")
if not isinstance(password, str):
    print("Ошибка: пароль должен быть строкой")
elif len(password) < 8:
    print("Слишком короткий пароль")
else:
    if "!" in password:
        print("Надёжный пароль")
    else:
        print("Добавьте спецсимволы")

# Task 3.2
year = input("Введите год: ")
if not year.isdigit() or int(year) == 0:
    print("Ошибка: год должен быть целым положительным числом!")
else:
    year = int(year)
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            print("Год високосный")
        else:
            print("Год не високосный")
    else:
        print("Год не високосный")