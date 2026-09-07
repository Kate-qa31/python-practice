# Part 1
books = [
    "Гордость и предубеждение",
    "Мастер и Маргарита",
    "Три товарища",
    "Сто лет одиночества",
    "Унесённые ветром",
    "Тень горы",
    "Цветы для Элджернона",
    "О дивный новый мир",
    "Норвежский лес",
    "Имя розы",
]

catalog = {
    "Джейн Остин": "Гордость и предубеждение",
    "Михаил Булгаков": "Мастер и Маргарита",
    "Эрих Мария Ремарк": "Три товарища",
    "Габриэль Гарсиа Маркес": "Сто лет одиночества",
    "Умберто Эко": "Имя розы",
}


total_pages = 1200
days = 0

# Task 1.1
def task_1(total_pages, days):
    try:
        result = total_pages // days
        print(f"Средняя скорость чтения: {result} страниц в день")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль недопустимо (ZeroDivisionError)")
    finally:
        print("Расчёт завершен!")

task_1(1200, 0)
task_1(1200, 10)

# Task 1.2
def task_2(books, ind):
    try:
        required_book = books[ind]
    except IndexError:
        print(f"Ошибка: книга с указанным индексом {ind} отсутствует! (IndexError)")
    else:
        print(f"Найденная книга: {required_book}")
    finally:
        print("Работа со списком книг завершена!")

task_2(books, 15)
task_2(books, 5)

# Task 1.3
def task_3(books, ind):
    try:
        number = int(books[ind])
    except ValueError:
        print("Ошибка: невозможно преобразовать (ValueError)")

task_3(books, 9)

# Task 1.4
def task_4(books, days):
    try:
        result = books + days
    except TypeError:
        print("Ошибка: операция между разными типами данных невозможна (TypeError)")
    finally:
        print("Получение суммы завершено!")

task_4(books, days)

# Task 1.5
def task_5(catalog, author):
    try:
        book_name = catalog[author]
    except KeyError:
        print(f"Ошибка: книга автора {author} отсутствует в каталоге (KeyError)")
    else:
        print(f"Искомая книга: {book_name}")
    finally:
        print("Поиск завершен!")

task_5(catalog, author = 'Михаил Булгаков')
task_5(catalog, author ='Сергей Довлатов')

# Task 1.6
def task_6():
    try:
        result = penalty_rate
    except NameError:
        print("Ошибка: переменная отсутствует (NameError)")

task_6()

# Task 1.7
def task_7():
    try:
        import recommendations_engine
    except ImportError:
        print("Ошибка при импорте модуля (ImportError)")

task_7()

# Task 1.8
def task_8(books, book_idx_str, mult):
    try:
        index = int(book_idx_str)
        my_book = books[index]
        result = index * mult
    except (TypeError, ValueError, IndexError):
        print("Ошибка: проверьте индекс и значение множителя")
    else:
        print(f"Найденная книга: '{my_book}', произведение индекса и параметра: {result}")
    finally:
        print("Работа функции завершена!")

task_8(books, book_idx_str = "2", mult = 3)
task_8(books, book_idx_str = "три", mult = 3)
task_8(books, book_idx_str = "5", mult = "4")
task_8(books, book_idx_str = "5", mult = None)
