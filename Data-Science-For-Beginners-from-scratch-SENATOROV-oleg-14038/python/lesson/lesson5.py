# +
"""Простой скрипт для ввода двух целых чисел и их вывода на экран."""

# num = int(input(':>'))
# num2 = int(input(':>'))
# print(num)
# print(num2)

# +
# print(1,2,3,4, sep='*', end='')#Перопределение ключевых  параметров
# sep - key ключ
# ='*' - val параметр
# print(1,2,3,4)

# +
# num = float(input('num'))
# num2 = float(input('num'))

# print('sum', num + num2) #
# print('Subtraction [səbˈtrakSH(ə)n]' , num - num2)
# print('Multiplication [məltəpləˈkāSH(ə)n]', num * num2)
# print('Division [dəˈviZHən] [dɪˈvɪʒən]', num / num2)

# +
# while True: # До : загаловок, а после инструкция
num = float(input("num1"))
operator = input("operator")
num2 = float(input("num2"))

if operator == "+":
    print("sum", num + num2)  #

elif operator == "-":
    print("Subtraction [səbˈtrakSH(ə)n]", num - num2)
elif operator == "*":
    print("Multiplication [məltəpləˈkāSH(ə)n]", num * num2)
elif operator == "/":
    print("Division [dəˈviZHən] [dɪˈvɪʒən]", num / num2)

# +
# def canculator(num, num2, operator):
# if operator == '+':
#     print('sum', num + num2) #
# elif operator == '-':
#      print('Subtraction [səbˈtrakSH(ə)n]' , num - num2)
#  elif operator == '*':
#     print('Multiplication [məltəpləˈkāSH(ə)n]', num * num2)
# elif operator == '/':
#   print('Division [dəˈviZHən] [dɪˈvɪʒən]', num / num2)

# while True: # До : загаловок, а после инструкция

#   num = float(input('num1'))
#  operator = input('operator')
# num2 = float(input('num2'))
# canculator(num, num2, operator)
