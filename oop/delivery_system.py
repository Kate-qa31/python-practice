# OOP practice based on course materials.
# Delivery system example: classes, inheritance,
# composition, enums, and object interaction.

import sys
from datetime import datetime
from enum import auto, StrEnum
from typing import Literal, Self


class Product:
    def __init__(
            self,
            product_id: int,
            name: str,
            weight: int,
            price: int,
            created_at: datetime,
    ):
        self.product_id = product_id
        self.name = name
        self.weight = weight
        self.price = price
        self.created_at = created_at


class User:
    def __init__(self, user_id: int, first_name: str, last_name: str, phone: str):
        self.id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class UserCustomer(User):
    def __init__(self, user_id: int, first_name: str, last_name: str, phone: str, address: dict[int, str]):
        super().__init__(user_id=user_id, first_name=first_name, last_name=last_name, phone=phone)
        self.address = address


class UserCourier(User):
    def __init__(self, user_id: int, first_name: str, last_name: str, phone: str, delivery_cost: int):
        super().__init__(user_id=user_id, first_name=first_name, last_name=last_name, phone=phone)
        self.delivery_cost = delivery_cost


class Storage:
    def __init__(self):
        self._shelf: dict[int, int] = {}

    def add_items(self, product_id: int, count: int = 1):
        self._shelf[product_id] = self._shelf.get(product_id, 0) + count

    def remove_items(self, good_id: int, count: int = 1):
        new_count = self._shelf.get(good_id, 0) - count
        if new_count < 0:
            raise ValueError("На складе нет достаточного количества товара с ID = {good_id")
        self._shelf[good_id] = new_count

class OrderStatus(StrEnum):
    created = auto()
    assembled = auto()
    closed = auto()


class Order:
    def __init__(self, orders: dict[int, Self]):
        self._orders = orders
        self._goods: dict[int, dict[Literal["count", "product"], int | Product]] = {}
        self._created_at: datetime | None = None
        self._status: OrderStatus | None = None


    def create(self, goods_ids: dict[int, int], goods: dict[int, Product]):
        next_id = max(self._orders, default=0) + 1
        self._goods = {
            product_id: {"count": count, "product": goods[product_id]}
            for product_id, count in goods_ids.items()
        }
        self._status = OrderStatus.created
        self._created_at = datetime.now()
        self._orders[next_id] = self


    def collect(self, storage: Storage):
        for product_id, product in self._goods.items():
            storage.remove_items(product_id, product["count"])
        self._status = OrderStatus.assembled


    def weight(self):
        return sum(p["count"] * p["product"].weight for p in self._goods.values())


    def price(self):
        return sum(p["count"] * p["product"].price for p in self._goods.values())


    def close(self):
        self._status = OrderStatus.closed

    def status(self):
        return self._status


class DeliveryStatus(StrEnum):
    created = auto()
    started = auto()
    delivered = auto()
    canceled = auto()


class Delivery:
    def __init__(self, order: Order, customer: UserCustomer):
        self._order = order
        self._customer = customer
        self._courier: UserCourier | None = None
        self._status: DeliveryStatus = DeliveryStatus.created

    def assign(self, courier: UserCourier):
        self._courier = courier

    def start(self) -> bool:
        if self._order.status() == OrderStatus.assembled and self._courier:
            self._status = DeliveryStatus.started
            return True
        return False

    def finish(self):
        self._order.close()
        self._status = DeliveryStatus.delivered

    def cancel(self):
        self._order.close()
        self._status = DeliveryStatus.canceled

    def address(self):
        return self._customer.address

    def status(self):
        return self._status


def get_goods() -> dict[int, Product]:
    return {
        1: Product(
            product_id=1, name="Говядина", weight=1000,
            price=120000, created_at=datetime(year=2025, month=12, day=1)
        ),
        2: Product(
            product_id=2, name="Горошек", weight=500,
            price=18000, created_at=datetime(year=2025, month=6, day=1)
        ),
        3: Product(
            product_id=3, name="Хлеб", weight=300,
            price=6000, created_at=datetime(year=2026, month=1, day=20)
        )
    }


def get_users() -> dict[int, User]:
    return {
        1: UserCustomer(
            user_id=1, first_name="Иннокентий", last_name="Петров",
            phone="+79991234567", address={1: "some street, 10"}
        ),
        2: UserCourier(
            user_id=2, first_name="Лучший", last_name="Сотрудник 1",
            phone="+79991234568", delivery_cost=300
        )
    }

if __name__ == "__main__":
    # Инициализируем справочник товаров:
    goods = get_goods()

    # Инициализируем справочник пользователей:
    users = get_users()

    # Создаём справочник заказов:
    orders: dict[int, Order] = {}

    # Создаём и наполняем склад:
    storage = Storage()
    storage.add_items(1, 10)
    storage.add_items(2, 10)

    # Создаём заказ:
    order_1 = Order(orders)
    order_1.create(goods_ids={1: 5, 2: 7}, goods=goods)

    # Создаём доставку:
    delivery_1 = Delivery(order=order_1, customer=users[1])

    # Назначаем курьера:
    delivery_1.assign(users[2])

    # Собираем заказ (и проверяем, возможно ли это):
    try:
        order_1.collect(storage)
    except ValueError as e:
        sys.exit(str(e))

    # Начинаем доставку:
    if not delivery_1.start():
        sys.exit("Не получилось начать доставку!")

    # Успешно доставляем по адресу и проверяем статусы:
    delivery_1.finish()

    print(delivery_1.status())
    print(order_1.status())