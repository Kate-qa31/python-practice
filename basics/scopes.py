# Part 1
# Task 1
salt = "морская"

def cook_pasta():
    salt = "поваренная"
    print("Внутри функции:", salt)

cook_pasta()
print("Снаружи функции:", salt)

# Task 2
pepper = "чёрный"

def change_pepper():
    pepper = "красный"
    print("Внутри функции:", pepper)

change_pepper()
print("Снаружи функции:", pepper) # Внутри функции создаётся локальная переменная pepper = "красный". Она скрывает глобальную pepper, но не изменяет её

# Task 3
pepper = "чёрный"

def change_pepper():
    global pepper
    pepper = "красный"
    print("Внутри функции:", pepper)

change_pepper()
print("Снаружи функции:", pepper) # global pepper указывает Python, что внутри функции нужно работать не с новой локальной переменной, а с глобальной pepper

# Task 4
eggs = 10

def use_eggs():
    eggs -= 1
    print("Внутри функции:", eggs)

# use_eggs() - ошибка: из-за присваивания Python считает eggs локальной переменной и при выполнеини eggs -= 1 пытается прочитать ее до того как ей присвоено значение
print("Снаружи функции:", eggs)

# Task 5
eggs = 10

def use_eggs():
    global eggs
    eggs -= 1
    print("Внутри функции:", eggs)

use_eggs() # изменилось значение глобальной переменной
print("Снаружи функции:", eggs)

# Task 6
def make_marinade():
    sauce = "кисло-сладкий"

    def add_secret_ingredient():
        sauce = "соевый"
        print("Значение переменной вложенной функции:", sauce)

    add_secret_ingredient() # изменилась только переменная вложенной функции
    print("Значение переменной внешней функции:", sauce)

make_marinade()

# Task 7
def make_marinade():
    sauce = "кисло-сладкий"

    def add_secret_ingredient():
        nonlocal sauce
        sauce = "соевый"
        print("Значение переменной вложенной функции:", sauce)

    add_secret_ingredient() # nonlocal позволяет изменить переменную из ближайшей enclosing-области видимости
    print("Значение переменной внешней функции:", sauce)

make_marinade()

# Task 8
def main_recipe():
    spice = "карри"

    def step():
        def detail_step():
            nonlocal spice
            spice = "паприка"
            print("Значение spice:", spice)

        detail_step()

    step()

main_recipe() # nonlocal ищет spice в enclosing-функциях и находит её в main_recipe()

# Task 9
def recipe():
    def inner():
        # nonlocal new_ing
        # new_ing = "шоколад"
        pass
    inner()

recipe()
# Если раскомментировать nonlocal new_ing, возникнет SyntaxError: переменной new_ing нет ни в одной enclosing-области

# Task 10
def prepare():
    main_ing = "томат"
    spice = "базилик"

    def adjust():
        nonlocal spice
        spice = "орегано"

    adjust()
    print(main_ing, spice)

prepare()

# Part 2
# Task 1
oil = "оливковое"

def cook_salad():
    oil = "подсолнечное"
    print("Внутри функции:", oil)

cook_salad()
print("Снаружи функции:", oil)

# Task 2
def pantry():
    stock = {"sugar": 5}

    def update_stock():
        nonlocal stock
        stock["sugar"] += 3

    update_stock()
    print(stock)

pantry()

# Task 3
flour = "пшеничная"

def bake_cake():
    flour = "кукурузная"

    def step():
        print("Внутри фунции step:", flour)

    step()
    print("Внутри bake_cake:", flour)

bake_cake()
print("Снаружи функции:", flour)

# Task 4
def make_dough():
    yeast = "сухие"

    def activate_yeast():
        yeast = "живые"

    activate_yeast()
    print("Внутри make_dough:", yeast)

make_dough()

# Task 5
sugar = 100

def bake():
    # sugar +=50 - изменение локальной переменной внутри функции приведет к ошибке, поскольку локальная переменная не объявлена
    print("Изменение значения внутри функции без global:", sugar)

bake()

# Task 6
spice = "паприка"

def outer():
    spice = "карри"

    def inner():
        print("Внутри функции inner:", spice)

    inner()

outer()
# Используется значение из enclosing области