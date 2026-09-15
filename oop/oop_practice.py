# Task 1
class TestCase:
    def __init__(self, name):
        self.name = name
        self.status = "Not Run"
    def run(self):
        self.status = "Passed"
    def show(self):
        print(f"{self.name}: {self.status}")

# Создай тест
test_login = TestCase("Проверка авторизации")

# Покажи статус (должно быть "Not Run")
test_login.show()

# Запусти тест
test_login.run()

# Покажи статус снова (должно быть "Passed")
test_login.show()

# Task 2
# Задача: «Разные типы тестов»
#
# Есть базовый класс Test. От него наследуются два разных типа тестов: PositiveTest (позитивный) и NegativeTest (негативный). У каждого типа свой результат.
#
# Условия:
# В классе Test:
# Принимает имя теста (name).
# Имеет метод get_result(), который возвращает строку "Not run".
#
# Класс PositiveTest наследуется от Test:
# Переопределяет метод get_result(), чтобы он возвращал "Passed".
#
# Класс NegativeTest наследуется от Test:
# Переопределяет метод get_result(), чтобы он возвращал "Failed".
#
# Вывод программы:
# Базовый тест: Not run
# Проверка входа с верным паролем: Passed
# Проверка входа с неверным паролем: Failed


# Макет решения:

# Описание класса
class Test:
    def __init__(self, name):
        self.name = name
    def get_result(self):
        return "Not Run"

class PositiveTest(Test):
    def get_result(self):
        return "Passed"

class NegativeTest(Test):
    def get_result(self):
        return "Failed"

# Создаем тесты

test1 = Test("Базовый тест")
test2 = PositiveTest("Проверка входа с верным паролем")
test3 = NegativeTest("Проверка входа с неверным паролем")

# Выводим результаты

print(f"{test1.name}: {test1.get_result()}")
print(f"{test2.name}: {test2.get_result()}")
print(f"{test3.name}: {test3.get_result()}")