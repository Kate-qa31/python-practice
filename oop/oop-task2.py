from dataclasses import dataclass

# Task 1
@dataclass
class Book:
    title: str
    author: str
    pages: int

    def __str__(self):
        return f"{self.title} — {self.author} ({self.pages})"

if __name__ == "__main__":
    required_book = Book(
        title="Властелин колец",
        author="Джон Р.Р. Толкин",
        pages=752
    )
    print(required_book)

# Task 2
class Temperature:
    def __init__(self, celsius: float) -> None:
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @property
    def fahrenheit(self) -> float:
        return (self._celsius * 9 / 5) + 32

if __name__ == "__main__":
    temp = Temperature(25)
    print(f"Температура в градусах Цельсия: {temp._celsius:.2f}, температура в градусах Фаренгейта: {temp.fahrenheit:.2f}")

