# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: base
#     language: python
#     name: python3
# ---

"""
This module provides basic arithmetic operations.

Functions.
- add_numbers(num1, num2): Returns the sum of two numbers.
"""


def greet(name1: str) -> None:
    """Print a greeting to the user.

    Args.
        name (str): The name of the person to greet.
    """
    print("Hello, " + name1)


numbers = [1, 2, 3, 4, 5]
print(numbers[4])


# +
def added(first: int, second: int) -> int:
    """Return the sum of two integers.

    Args.
        a (int): The first integer to add.
        b (int): The second integer to add.

    Return.
        int: The sum of a and b.
    """
    return first + second


result3 = added(10, 21)
print(result3)
# -

name = "Alice"
print("Hello, " + name)

x_deb = 10
y_deb = 5
try:
    result1: int = int(x_deb / y_deb)
    print(result1)
except ZeroDivisionError:
    print("Ошибка: деление на ноль.")
except ValueError:
    print("Ошибка: неверное значение для преобразования.")

num = 10
text = "10"
if num == int(text):
    print("Числа равны")


# +
def adds(a_fer: int, b_sec: int) -> int:
    """Add two integers and returns the result_one.

    Arg.
        a (int): The first integer to add.
        b (int): The second integer to add.

    Return.
        int: The sum of the two integers.
    """
    return a_fer + b_sec


result_one = adds(10, 5)
print(result_one)


# +
def add_numbers(num1: int, num2: int) -> int:
    """Add two numbers and returns the result_two.

    Arg.
        a (int): The first number.
        b (int): The second number.

    Return.
        int: The sum of the two numbers.
    """
    result_two = num1 + num2

    return result_two


print(add_numbers(5, 10))
