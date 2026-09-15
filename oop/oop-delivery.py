# Task 1
import enum


class Room:
    def __init__(
            self,
            room_number: int,
            is_booked: bool,
            persons: int,
            floor: int,
            price: int
    ) -> None:
        self.room_number = room_number
        self.is_booked = is_booked
        self.persons = persons
        self.floor = floor
        self.price = price

room_1 = Room(
    room_number=1,
    is_booked=False,
    persons=2,
    floor=1,
    price=100
)
room_2 = Room(
    room_number=2,
    is_booked=False,
    persons=4,
    floor=1,
    price=200
)
class BathSize(enum.IntEnum):
    small=1
    medium=2
    large=3

class LuxuryRoom(Room):
    def __init__(
            self,
            room_number: int,
            is_booked: bool,
            persons: int,
            floor: int,
            price: int,
            bath_size: BathSize
    ) -> None:
        super().__init__(room_number=room_number, is_booked=is_booked, persons=persons, floor=floor, price=price)
        self.bath_size = bath_size

room_3 = LuxuryRoom(
    room_number=3,
    is_booked=False,
    persons=1,
    floor=2,
    price=500,
    bath_size=BathSize.large
)

room_4 = LuxuryRoom(
    room_number=4,
    is_booked=False,
    persons=1,
    floor=2,
    price=450,
    bath_size=BathSize.medium
)
print(BathSize.large)
print(BathSize.large.name)
print(BathSize.large.value)