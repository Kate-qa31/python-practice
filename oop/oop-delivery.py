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

    def book(self) -> None:
        self.is_booked = True

    def cancel_booking(self) -> None:
        self.is_booked = False

    @property
    def is_available(self) -> bool:
        return not self.is_booked

class Hotel:
    def __init__(
            self,
            name: str,
            location: str
    ) -> None:
        self.name = name
        self.location = location
        self.rooms: dict[int, Room] = {}

    def add_rooms(self, rooms: list [Room]) -> None:
        for room in rooms:
            self.rooms[room.room_number] = room

    def show_available_rooms(self) -> list[Room]:
        available_rooms = []
        for room in self.rooms.values():
            if room.is_available:
                available_rooms.append(room)
        return available_rooms

    def get_room(self, room_number: int) -> Room:
            try:
                return self.rooms[room_number]
            except KeyError:
                raise ValueError(f"There is no room with number {room_number}")
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

if __name__ == "__main__":
    ### Подготовка отеля:
# Комната 1:
    room_1 = Room(
        room_number=1,
        is_booked=False,
        persons=2,
        floor=1,
        price=100
    )

    # Комната 2:
    room_2 = Room(
        room_number=2,
        is_booked=False,
        persons=4,
        floor=1,
        price=200
    )

    # Комната 3:
    room_3 = LuxuryRoom(
        room_number=3,
        is_booked=False,
        persons=1,
        floor=2,
        price=500,
        bath_size=BathSize.large
    )

    # Комната 4:
    room_4 = LuxuryRoom(
        room_number=4,
        is_booked=False,
        persons=1,
        floor=2,
        price=450,
        bath_size=BathSize.medium
    )

    # Создаём отель:
    hotel = Hotel(
        name="Астория",
        location="Северный полюс"
    )

    # Создаём набор комнат:
    rooms = [room_1, room_2, room_3, room_4]

    hotel.add_rooms(rooms)

    available_rooms = hotel.show_available_rooms()

    available_rooms[0].book()

    assert not available_rooms[0].is_available