# Part 1
countries = ['Италия', 'Франция', 'Япония', 'Норвегия', 'Чили', 'Канада', 'Перу']
companions = ['Анна', 'Олег', 'Ирина', 'Михаил', 'Светлана']
places = ['Эйфелева башня', 'Колизей', 'Фудзи', 'Биг-Бен', 'Ниагарский водопад']

# Task 1.1
import random
random_country = random.choice(countries)
print(f"Случайная страна: {random_country}")

# Task 1.2
import random
day = random.randint(1, 31)
print(f"Случайный день: {day}")

# Task 1.3
import random
rate = random.uniform(0.9, 0.95)
print(f"Случайный курс: {rate:.2f}")

# Task 1.4
import random
place = random.choices(places, k=3)
print(place)

# Task 1.5
import random
country_for_traveling = random.sample(countries, k=3)
print(country_for_traveling)

# Task 1.6
import random
chance = random.randint(0, 100)
if chance >= 70:
    print(f"Шанс на визу: {chance}%. Виза одобрена")
else:
    print(f"Шанс на визу: {chance}%. Виза отклонена")

# Additional tasks
# Task 1.1
import random
flight_number = random.randint(1000, 9999)
print(f"Случайный номер рейса: {flight_number}")

# Task 1.2
import random
discount = random.randint(5, 30)
print(f"Скидка на билет: {discount}%")

# Task 1.3
import random
companion = random.choice(companions)
print(f"Случайный попутчик: {companion}")

# Task 1.4
import random
budget = random.uniform(800, 2000)
print(f"Бюджет поездки: €{budget:.2f}")

# Part 2
# Task 2.1
from datetime import datetime
date_str = "10-04-1925"
parsed = datetime.strptime(date_str, "%d-%m-%Y")
print(parsed)
print(type(parsed))

# Task 2.2
from datetime import date, timedelta
today = date.today()
finished_date = today + timedelta(days=14)
print(finished_date)

# Task 2.3
from datetime import time
exact_time = time(21, 30)
print(exact_time)

# Task 2.4
from datetime import date
today = date.today()
formatted_date = today.strftime("%d.%m.%Y")
print(formatted_date)

# Task 2.5
from datetime import date
book1 = date(2005, 1, 1)
book2 = date(2015, 1, 1)

if book1 < book2:
    print("Вторая книга новее")
else:
    print("Первая книга новее")

# Task 2.6
from datetime import datetime
publication_date = datetime(2021, 2, 14, 18, 45)
print(publication_date)

# Task 2.7
from datetime import datetime
now = datetime.now()
now_formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(now_formatted)

# Additional tasks
# Task 2.1
from datetime import date
publish_date = date(2010, 5, 5)
print(publish_date)

# Task 2.2
from datetime import date
current_date = date.today()
print(f"Номер текущего дня месяца: {current_date.day}, количество дней с начала месяца: {current_date.day-1}")

# Task 2.3
from datetime import date
today = date.today()
book_published = date(1925,4,10)
year_book_published = book_published.year
year_difference = today.year - year_book_published
age = year_difference - ((today.month, today.day) < (book_published.month, book_published.day))
print(f"Книге, изданной 10 апреля 1925 года, {age} полных лет")

# Part 3
# Task 3.1
import math
width = 16
height = 9
d = math.sqrt(math.pow(width, 2) + math.pow(height, 2))
print(f"Диагональ: {d:.2f} м")

# Task 3.2
import math
sits = 267
capacity = 20
quantity_of_raws = math.floor(sits / capacity)
print(f"{quantity_of_raws} полных рядов")

# Task 3.3
import math
quantity_of_movies = 3
duration_of_movies = 12
total_duration_minutes = quantity_of_movies * duration_of_movies
total_duration_hours = math.ceil(total_duration_minutes / 60)
print(f"Общее время показа фильмов составило примерно {total_duration_hours} час")

# Task 3.4
import math
diameter = 4
length = diameter * math.pi
print(f"Длина окружности составляет {length:.2f} см")

# Task 3.5
import math
t = 2
interest = 100 * math.e ** (-0.3 * t)
print(f"Интерес зрителя через 2 часа: {interest:.2f}")

# Task 3.6
import math
cases = math.factorial(5)
print(f"Зрителей можно рассадить {cases} разными способами")

# Additional tasks
# Task 3.1
import math
d = 3.5
l = 1000 / math.pow(d, 2)
print(f"Уровень освещения: {l:.2f}")

# Task 3.2
import math
tickets_capacity = 7
tickets_quantity = 50
uses = math.ceil(tickets_quantity / tickets_capacity)
print(f"Посетитель воспользуется автоматом {uses} раз")

# Task 3.3
movie_duration = 113
hours = math.floor(movie_duration / 60)
print(f"Количество полных часов фильма: {hours}")

# Task 3.4
duration = 137
interval = 30
next_time = math.ceil(duration / interval) * interval
print(f"Ближайшее следующее время (в минутах): {next_time}")

# Part 4
# Task 4.1
book = {
	"title": "1984",
	"author": "George Orwell",
	"year": 1949,
	"genres": ["dystopia", "political fiction", "science fiction"],
	"pages": 328,
	"available": True,
	"rating": 4.7
}
import json
json_string = json.dumps(book, ensure_ascii=False)
print(json_string)

# Task 4.2
data = '''
[
	{
    	"title": "1984",
    	"author": "George Orwell",
    	"year": 1949,
    	"genres": ["dystopia", "political fiction"]
	},
	{
    	"title": "Brave New World",
    	"author": "Aldous Huxley",
    	"year": 1932,
    	"genres": ["dystopia", "science fiction"]
	},
	{
    	"title": "Fahrenheit 451",
    	"author": "Ray Bradbury",
    	"year": 1953,
    	"genres": ["dystopia", "speculative fiction"]
	}
]
'''
import json
books_info = json.loads(data)
print(f"Автор первой книги: {books_info[0]["author"]}")

# Task 4.3
library = {
	"library_name": "Central Library",
	"location": "Main Street, 10",
	"books": [
    	{"title": "1984", "author": "George Orwell", "available": True},
    	{"title": "Brave New World", "author": "Aldous Huxley", "available": False},
    	{"title": "Fahrenheit 451", "author": "Ray Bradbury", "available": True}
	]
}

import json
library_info = json.dumps(library, ensure_ascii=False)
print(library_info)

# Task 4.4
json_data = '''
[
	{"title": "1984", "author": "George Orwell", "available": true},
	{"title": "Brave New World", "author": "Aldous Huxley", "available": false},
	{"title": "Fahrenheit 451", "author": "Ray Bradbury", "available": true}
]
'''
import json
books_information = json.loads(json_data)
for book in books_information:
    if book["available"] == True:
        print(book["title"])