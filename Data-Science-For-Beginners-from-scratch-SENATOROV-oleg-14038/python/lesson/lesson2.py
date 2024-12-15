# +
"""Модуль для поиска наибольшего значения в списке чисел."""

numbers = [1, 2, 3]  # список - Структура данных

# алгоритм поиска наибольшего значения
# Алгоритм = последовательность действий, для выполнения задачи

max_value = numbers[0]  # Создали новую переменную max_value
# и присвоили ей значение элемента с индексом ноль

for number in numbers:  # in оператор членства
    max_value = max(max_value, number)  # Используем встроенную
    # функцию max для обновления max_value

print(max_value)  # Максимальный элемент
# -

# ### Алгоритм - написание калькулятор
# ### 1) Ввести число
# ### 2) Действие
# ### 3) Ввести второе число
# ### 4) вывести результат

# +
operation_list = ["+", "-", "/", "*"]


def calculate(num_1: float, math_: str, num_2: float) -> float | int:
    """Выполняет математическую операцию с двумя числами и выводит результат на
    консоль.

    Параметры:
    num_1 (float): Первое число.
    math_ (str): Математическая операция (+, -, /, *).
    num_2 (float): Второе число.

    Возвращает:
    float: Результат вычислений. Если произошла ошибка, возвращает 0.0.
    """
    try:
        if math_ == "/" and num_2 == 0:
            print("Ошибка: Деление на ноль")
            return 0.0

        if math_ == "+":
            result = num_1 + num_2
        elif math_ == "-":
            result = num_1 - num_2
        elif math_ == "/":
            result = num_1 / num_2
            result = int(result) if result.is_integer() else result
        elif math_ == "*":
            result = num_1 * num_2
        else:
            print("Неизвестная операция")
            return 0.0

        print(f"{num_1} {math_} {num_2} = {result}")
        return result

    except ValueError:
        print("Ошибка: Неверные входные данные")
        return 0.0
