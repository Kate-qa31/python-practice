import sys
from datetime import date
import psycopg
from tabulate import tabulate

class HotelAdmin:

    def __init__(self, conn_params):
        self.conn_params = conn_params
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg.connect(**self.conn_params)
            print("Успешное подключение к базе данных")
            return True
        except psycopg.Error as e:
            print(f"Ошибка подключения: {e}", file=sys.stderr)
            return False

    def close(self):
        if self.conn:
            self.conn.close()

    def show_available_rooms(self):
        print("\nПоиск доступных номеров")

        check_in = input("Дата заезда (ГГГГ-ММ-ДД): ")
        check_out = input("Дата выезда (ГГГГ-ММ-ДД): ")

        with self.conn.cursor() as cur:
                cur.execute("""
                            SELECT
                                r.id,
                                h.name AS hotel,
                                h.address AS address,
                                h.city AS city,
                                r.room_number,
                                rt.name AS type,
                                r.price_per_night,
                                r.capacity
                            FROM rooms r
                            JOIN hotels h ON r.hotel_id = h.id
                            JOIN room_types rt ON r.room_type_id = rt.id
                            WHERE r.is_available = TRUE
                            AND r.id NOT IN (
                                SELECT room_id FROM bookings
                                WHERE status = 'confirmed'
                                AND (check_in_date, check_out_date) OVERLAPS (%s::date, %s::date + INTERVAL '1 day')
                            )
                            ORDER BY r.price_per_night
                        """, (check_in, check_out))

                print("\nДоступные номера:")
                results = []
                for row in cur:
                    results.append({
                        'ID': row[0],
                        'Отель': f"{row[1]} ({row[2]}, {row[3]})",
                        'Номер': row[4],
                        'Тип': row[5],
                        'Цена/ночь': f"{row[6]} руб.",
                        'Мест': row[7]
                    })
                print(tabulate(results, headers="keys", tablefmt="grid", stralign="left"))
    def find_guests_by_dates(self):
        print("\nСписок гостей отеля (для полиции)")
        hotel_id = input("ID отеля: ")
        start_date = input("Начальная дата (ГГГГ-ММ-ДД): ")
        end_date = input("Конечная дата (ГГГГ-ММ-ДД): ")

        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT DISTINCT
                        u.id,
                        u.full_name,
                        u.phone,
                        u.email,
                        b.check_in_date,
                        b.check_out_date,
                        r.room_number
                    FROM bookings b
                    JOIN users u ON b.user_id = u.id
                    JOIN rooms r ON b.room_id = r.id
                    WHERE r.hotel_id = %s
                    AND b.status = 'completed'
                    AND (b.check_in_date, b.check_out_date) OVERLAPS (%s::date, %s::date + INTERVAL '1 day')
                    ORDER BY b.check_in_date
                """, (hotel_id, end_date, start_date))

                print("\nГости отеля:")
                results = []
                for row in cur:
                    results.append({
                        'ID': row[0],
                        'Имя': row[1],
                        'Телефон': row[2],
                        'Email': row[3],
                        'Проживал': f'{row[4]} - {row[5]}',
                        'Номер': row[6],
                    })
                print(tabulate(results, headers="keys", tablefmt="grid", stralign="left"))
        except psycopg.Error as e:
            print(f"Ошибка при поиске гостей: {e}")

    def create_booking(self):
        print("\nСоздание бронирования")
        user_id = input("ID пользователя: ")
        room_id = input("ID номера: ")
        check_in = input("Начальная дата (ГГГГ-ММ-ДД): ")
        check_out = input("Конечная дата (ГГГГ-ММ-ДД): ")

        try:
            with self.conn.transaction():
                with self.conn.cursor() as cur:
                    cur.execute("""
                        SELECT r.price_per_night, r.hotel_id
                        FROM rooms r
                        WHERE r.id = %s
                        AND r.is_available = TRUE
                        AND NOT EXISTS (
                            SELECT 1 FROM bookings
                            WHERE room_id = %s
                            AND status = 'confirmed'
                            AND (check_in_date, check_out_date) OVERLAPS (%s::date, %s::date + 1)
                        )
                        """, (room_id, room_id, check_in, check_out))

                    res = cur.fetchone()
                    if not res:
                        raise psycopg.Error("Номер недоступен для бронирования в указанные даты")

                    price = res[0]
                    hotel_id = res[1]
                    total = price * (date.fromisoformat(check_out) - date.fromisoformat(check_in)).days

                    booking_id = cur.execute("""
                        INSERT INTO bookings (
                            user_id, hotel_id, room_id, check_in_date,
                            check_out_date, total_price, status
                        ) VALUES (%s, %s, %s, %s, %s, %s, 'confirmed')
                        RETURNING id
                    """, (user_id, hotel_id, room_id, check_in, check_out, total)).fetchone()[0]

                    print(f"Бронирование #{booking_id} создано. Сумма: {total} руб.")

        except psycopg.Error as e:
            print(f"Ошибка при создании бронирования: {e}")

    def delete_bad_review(self):
        print("\nУдаление негативного отзыва")
        review_id = input("ID отзыва: ")

        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    DELETE FROM reviews
                    WHERE id = %s AND rating <= 2
                    RETURNING id, rating, comment
                """, (review_id,))

                deleted = cur.fetchone()
                if not deleted:
                    raise psycopg.Error("Отзыв не найден или имеет положительную оценку")

                self.conn.commit()
                print(f"Удален отзыв #{deleted[0]} с оценкой {deleted[1]}: {deleted[2]}")
        except psycopg.Error as e:
            self.conn.rollback()
            print(f"Ошибка при удалении отзыва: {e}")

    def show_menu(self):
        print("\nМеню администратора отеля:")
        print("1. Найти доступные номера (чтение)")
        print("2. Список гостей за период (чтение)")
        print("3. Создать бронирование (вставка)")
        print("4. Удалить негативный отзыв (удаление)")
        print("0. Выход")

    def run(self):
        if not self.connect():
            return

        menu_actions = {
            '1': self.show_available_rooms,
            '2': self.find_guests_by_dates,
            '3': self.create_booking,
            '4': self.delete_bad_review
        }

        try:
            while True:
                self.show_menu()
                choice = input("Выберите действие: ").strip()

                if choice == '0':
                    print("Выход из системы...")
                    break

                action = menu_actions.get(choice)
                if action:
                    action()
                else:
                    print("Неверный ввод. Попробуйте еще раз")

        except KeyboardInterrupt:
            print("\nЗавершение работы по запросу пользователя")
        finally:
            self.close()


if __name__ == "__main__":
    # Локальная учебная БД, запускается через Docker Compose
    conn_params = {
        "dbname": "hotels_booking_db",
        "user": "hotels_booking_user",
        "password": "hotels_booking_pass",
        "host": "localhost",
        "port": 5432,
    }

    app = HotelAdmin(conn_params)
    app.run()