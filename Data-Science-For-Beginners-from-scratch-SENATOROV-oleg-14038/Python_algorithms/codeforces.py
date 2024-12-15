# +
"""The code snippet `import sys`: imports the sys module in Python.

This module provides access to some variables used or maintained by the
interpreter and to functions that interact with the interpreter.
"""

import sys

# -

# #### https://codeforces.com/problemset?order=BY_RATING_ASC&tags=math
#

# +
watermelon_weight = int(input("Введите вес арбуза: "))

# Решение 1:
if watermelon_weight % 2 == 0 and watermelon_weight > 2:
    print("YES")
else:
    print("NO")
# -

# #### https://codeforces.com/problemset/problem/50/A

# +
input_values1 = input()
base, height = (int(i) for i in input_values1.split())
print(int(base * height / 2))


# 1) Функция input() используется для получения ввода
# от пользователя и сохраняет введенные данные
# в переменную list1 в виде строки
# 2)Затем метод split() разбивает введенную
# строку на отдельные элементы,
# используя пробел в качестве разделителя
# Результат разбиения преобразуется в список, и затем значения
# в этом списке преобразуются в целые числа,
# используя comprehensions в цикле for.
# Как результат, a и b получают значения этих целых чисел.
# Далее программа вычисляет площадь треугольника
# по формуле (a  b) / 2 и
# выводит результат с помощью функции print().
# -

# #### https://codeforces.com/problemset/problem/158/A

# +
distance = int(input())
# Этот код принимает входные данные distance
# и вычисляет количество необходимых шагов.

if distance % 5 == 0:  # Если distance делится на 5
    steps_needed = distance // 5
# он вычисляет шаги как distance // 5
else:
    steps_needed = distance // 5 + 1
# В противном случае он добавляет 1 к результату

print(steps_needed)


# +
def calculate_steps() -> None:
    """Вычисляет минимальное количество шагов.

    Необходимых слону для достижения целевой позиции.
    """
    destination = int(
        input("Введите целевую позицию: "),
    )  # Ввод пользователя и преобразование в целое число
    current_position = 0  # Текущее положение слона
    steps_count = 0  # Количество выполненных шагов
    # Проверка, что введенное значение находится в допустимом диапазоне
    if 1 <= destination <= 10**6:
        while current_position < destination:
            # Цикл продолжается, пока текущее положение слона меньше целевого
            # Если целевая позиция больше или равна 5
            if destination >= 5:
                # Слон делает 5 шагов вперед
                current_position += 5
                # Увеличиваем количество шагов
                steps_count += 1
            elif destination == 4:
                current_position += 4
                steps_count += 1
            elif destination == 3:
                current_position += 3
                steps_count += 1
            elif destination == 2:
                current_position += 2
                steps_count += 1
            elif destination == 1:
                current_position += 1
                steps_count += 1

    print(steps_count)


if __name__ == "__main__":
    calculate_steps()
# -

# https://codeforces.com/problemset/problem/546/A

# +
number_two = int(input())
print(number_two / 2 - number_two * (number_two % 2))

# 1. В первой строке кода n=input()
# происходит ввод значения переменной n с клавиатуры.
# Введенное значение будет рассматриваться как строка.
# 2. Далее, во второй строке кода print n/2-n*(n%2)
# происходит вычисление выражения и его вывод на экран.
# 1.1  - n*(n%2) означает умножение значения
# n на остаток от деления n на 2.
# Здесь % является оператором получения остатка от деления.
# В данном случае, если n четное, остаток
# от деления будет равен 0,
# а если n нечетное, остаток будет равен 1.
# 1.2 - n/2 означает деление значения n на 2
# Результат этого деления будет вещественным числом.
# Если введенное значение n было целым числом,
# это деление также будет вещественным числом.

# Итак, выражение n/2-n*(n%2) означает разность
# между половиной значения n и
# произведением значения n на его остаток от деления на 2.


# +
def calculate_half_number(first_number: int) -> int:
    """Функция принимает целое число и возвращает результат вычислений."""
    if first_number % 2 == 0:
        return first_number // 2
    return (-first_number - 1) // 2


# input(): функция возращает введенную пользователем строку до нажатия enter
user_input = int(input())
print(calculate_half_number(user_input))

# +
total_numbers = int(input())  # Ввод целого числа от пользователя
odd_count = 0
even_count = 0

if total_numbers == 1:
    print("-1")  # Если n равно 1, выводим "-1"
else:
    if total_numbers % 2 == 0:
        odd_count = total_numbers // 2
        even_count = total_numbers // 2
    else:
        odd_count = total_numbers // 2 + 1
        even_count = total_numbers // 2

    odd_start = -1
    even_start = 2

    if total_numbers % 2 == 0:
        odd_end = -(total_numbers - 1)
        even_end = total_numbers - 2  # Инициализация для четного случая
    else:
        odd_end = -total_numbers
        even_end = total_numbers - 1

    sum_odd = (odd_count * (odd_start + odd_end)) // 2
    sum_even = (even_count * (even_start + even_end)) // 2

    print(sum_odd + sum_even)


# -

# https://codeforces.com/problemset/problem/486/A


# +
def calculate_function(even_number: int) -> float:
    """Функция принимает целое число и возвращает результат вычислений:.

    - Если число четное, возвращает его половину.
    - Если число нечетное, возвращает отрицательное.
    значение половины этого числа, увеличенного на 1.

    :param even_number: Целое число.
    :return: Результат вычислений в виде числа с плавающей точкой.
    """
    even_number = int(input())

    if even_number % 2 == 0:
        return even_number / 2

    return (even_number + 1) / 2 * (-1)


even_numbe1 = int(input())

result_first = calculate_function(even_numbe1)

print(result_first)

# 1)Запрашивает пользователя ввести
# значение целого числа `n`
# 2)Вызывает функцию `CalFunc(n)`,
# передавая введенное значение `n` в качестве аргумента.
# 3)Выводит целую часть результата вызова `CalFunc(n)`.

# Примечание
# Например, если было введено значение 5,
# то функция `CalFunc(5)` вернет `-3,
# так как (5+1)/2*(-1) = -3.
# Основная программа затем выведет целую
# часть -3, которая равна -3.

# Таким образом, данная программа принимает число `n`,
# применяет к нему определенную математическую
# функцию в зависимости от того,
# является ли оно четным или нечетным,
# и выводит целую часть результата.

# +
valueofn = int(input())

if valueofn % 2 == 0:
    output = valueofn // 2
else:
    output = ((valueofn + 1) // 2) * (-1)

print(output)
# -

# https://codeforces.com/problemset/problem/200/B

# +
print(1 / int(input()) * sum(map(int, input().split())))

# 1. input() вызывается, чтобы принять ввод пользователя.
# ункция input() приостанавливает выполнение программы и ожидает,
# пока пользователь введет строку с клавиатуры.
# Введенная строка будет
# считываться как делимое в следующей части выражения.

# 2. int(input()) берет введенную строку и преобразует ее в целое число.
# Таким образом, пользовательский ввод будет
# интерпретироваться как делитель в дальнейшем выражении.

# 3. input().split() считывает ввод п��льзователя, а затем разбивает
# его на отдельные элементы по пробелам.
# Функция split() без аргументов разделяет строку на отдельные слова.
# Распакуется в список слов,
# которые будут использованы в следующей части выражения.

# 4. map(int,input().split()) берет каждый элемент списка,
# полученного из ввода пользователя,
# и преобразует его в целое число с помощью функции int().
# Таким образом,
# все введенные пользователем значения будут преобразованы в числа.

# 5. sum(map(int,input().split())) складывает все числа в списке,
# полученном из ввода пользователя.

# 6. 1/int(input()) берет введенное пользователем
# число и вычисляет его обратную величину.

# 7. * выполняет умножение между обратной величиной
# числа и суммой чисел из ввода пользователя.

# 8. print() выводит результат в stdout (стандартный поток вывода).
# -

# #### https://codeforces.com/problemset/problem/200/B

# +
count_of_numbers = int(input())  # Ввод общего количества чисел
numbers = list(map(int, input().split()))
# Ввод чисел и преобразование их в список целых чисел

sum_of_numbers = 0
# Инициализация переменной для хранения суммы чисел
for number in numbers:
    sum_of_numbers += number
# Добавление текущего числа к сумме

average = sum_of_numbers / count_of_numbers
# Вычисление среднего значения
print(average)
# Вывод среднего значения
# -

# #### https://codeforces.com/problemset/problem/200/B
#
#


# +
def main() -> float:
    """Основная функция программы.

    которая вычисляет среднее значение. набора целых чисел, введенных
    пользователем.

    :return: Среднее значение всех введенных. чисел в виде числа с плавающей
    точкой.
    """
    # Ввод количества элементов
    number_of_elements = int(sys.stdin.readline())
    # Ввод элементов и преобразование их в список целых чисел
    elements = map(int, sys.stdin.readline().split())

    # Вычисление суммы всех элементов
    total_sum = sum(elements)
    avg_value = total_sum / number_of_elements
    # Вычисление среднего значения

    return avg_value


# Вывод среднего значения
if __name__ == "__main__":
    print(main())
# -

# #### https://codeforces.com/problemset/problem/1328/A

# +
number_three = int(input())  # `number = int( input() )` -
# Принимает целое число с клавиатуры и сохраняет его в переменной `number`.

result = []  # 2. `result = [ ]` -
# Создает пустой список с именем `result`,
# который будет содержать результаты остатков от деления.


for num in range(number_three):
    # 3. `for num in range( number ) :`
    # Начинается цикл, который будет выполняться `number` раз, где `number` -
    # это число, введенное пользователем на первом шаге.

    string = input().split()  # 4. `string = input().split()`
    # - Принимает ввод с клавиатуры и разбивает его на отдельные слова,
    # сохраняя в виде списка в переменной `string`.

    num1 = int(string[0])  # num1 = int( string[ 0 ] )`
    # Преобразует первый элемент списка `string`
    # в целое число и сохраняет в переменной `num1`.
    num2 = int(string[1])  # num2 = int( string[ 1 ] )`-
    # Преобразует второй элемент списка `string`
    # в целое число и сохраняет в переменной `num2`.

    if num1 >= num2:  # 7. `if ( num1 >= num2 ) :`-
        # Проверяет, является ли `num1` больше или равным `num2`.

        if num1 % num2 == 0:  # 8. `if ( num1 % num2 == 0 )
            # Проверяет, равен ли остаток
            # от деления `num1` на `num2` нулю.

            result.append(0)  # 9. `result.append( 0 )`-
        # Если условия выполнены, добавляет `0` в список `result`.
        else:

            remainder = num2 - (num1 % num2)

            result.append(remainder)

    else:

        remainder = num2 - num1

        result.append(remainder)

for output in result:

    print(output)


# +
def calculate_modulo_difference() -> None:
    """Главная функция, которая выполняет.

    расчет для каждой пары чисел, введенных пользователем.
    """
    test_cases: int = int(input("Введите кол тестовых случаев: "))

    for _ in range(test_cases):
        dividend, divisor = map(
            int,
            input("Введите два числа, разделенные пробелом: ").split(),
        )
        result_the_same = (divisor - dividend % divisor) % divisor
        print(result_the_same)


if __name__ == "__main__":
    calculate_modulo_difference()
