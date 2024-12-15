"""Module contains functions for checking the status of a door and performing.

appropriate actions such as unlocking or opening it.
"""

# +
# # def check_and_open_door(door_is_closed, door_is_locked: Any)-> None:
#     """Check door status and perform actions."""
#     if door_is_closed:
#         if door_is_locked:
#             unlock_door()  # вызов функции для разблокировки двери
#         open_door()  # вызов функции для открытия двери

#     advance()  # вызов функции для продолжения выполнения

# +
# def print_prime_numbers():
#     """Print prime numbers in a specified range."""
#     start_range = 2
#     end_range = 10

#     for number in range(start_range, end_range):
#         for potential_divisor in range(start_range, number):
#             if number % potential_divisor == 0:  # проверка делимости
#                 break
#         else:
#             # цикл завершился без нахождения делителя
#             print(number)

#     # Печать объекта range, для демонстрации
#     print(range(start_range, end_range))


# # Вызов функций
# check_and_open_door(door_is_closed=True, door_is_locked=False)
# # print_prime_numbers()
