"""Чистый код."""

# # Глава 1. Трассировка ошибок
#
# Traceback (most recent call last):
#
#   File "main.py", line 10, in <module>
#
#     result = divide(10, 0)
#
#   File "main.py", line 5, in divide
#
#     return a / b
#
# ZeroDivisionError: division by zero
#
# Читать нужно снизу вверх
#
# Последняя строка содержит тип ошибки и её описание
#
# Выше показан путь к месту ошибки

# # Глава 2 Подготовка среды и командная строка
#
# Подготовкой среды называется процесс настройки вашего
# компьютера для программирования.
#
# В Windows для разделения имен папок и файлов используется символ \ (обратная
# косая черта), а в macOS и Linux разделителем является символ / (косая черта).
#
# Программы командной оболочки:
#
#  Bourne Shell (sh) - Linux
#
#  Bourne-Again Shell (bash) - Linux
#
#  Z shell (zsh) - MacOS
#
#  Командная строка - Windows
#
#  **Аргументы командной строки** - текстовые фрагменты, которые
# вводятся после имени команды. Как и аргументы, передаваемые при вызове функций
# Python, они предоставляют команде дополнительную информацию или указания.
# Например, при выполнении команды cd C:\Users часть C:\Users является аргументом
# команды cd, которая сообщает команде, какая папка должна стать текущим рабочим
# каталогом. Или при запуске сценария Python из окна терминала командой python
# yourScript.py часть yourScript.py является аргументом, который сообщает программе python, в каком файле следует искать выполняемую последовательность команд.
#
# **Ключи командной строки** - краткие аргументы, часто начинаются с - или --
#
# **Поиск файлов начинающихся с определенного символа:**
#
# al@al-VirtualBox:~$ cd D
#
# Desktop/ Documents/ Downloads/
#
# al@al-VirtualBox:~$ cd D
#
# При нажатии клавиши ↑ в терминале командная строка заполняется
# последней введенной вами командой. Дальнейшие нажатия клавиши ↑ продолжают
# перебирать более ранние команды, а нажатия клавиши ↓ возвращают к более поздним командам. Если вы хотите отменить команду в приглашении и начать с нового
# приглашения, нажмите Ctrl-C.
#
# **Изменение текущего рабочего каталога. Работа с ним.**
#
# # cd [папка]
#
# Команда ls выводит список всех папок и файлов находящихся в рабочем каталоге
#
# Чтобы вывести подробную информацию
# с размером файла, разрешениями, временными метками последнего изменения
# и другой информацией, используйте ключ -l.
#
# Чтобы команда ls выводила все файлы, включая скрытые,
# используйте ключ -a.
#
# find выводит содержимое текущего рабочего каталога
# и его подкаталогов.
#
# find . -name "*.py"
#
# Символ . приказывает find начать поиск в текущем рабочем каталоге. С ключом
# -name команда find ищет папки и файлы по имени. Фрагмент "*.py" приказывает
# find искать папки и файлы с именами, соответствующими шаблону *.py. Следует
# заметить, что команда find требует, чтобы аргумент после -name был заключен
# в двойные кавычки.
#
# # cp hello.py someSubFolder - скопировать нужный файл в нужное место: cd [нужный файл][нужное место]
#
# команда mv [файл или папка] [новое имя] переименовывает файл
#
# # mv hello.py goodbye.py
#
# # rm [файл] - удалить файл
#
# # rm -r [папка] - удалить папку
#
# mkdir[новая папка] - создать новую папку
#
# which [программа] - сообщает точное местонахождение программы
#
# clear - стирает весь текст в окне терминала
#
# ## Переменная среда PATH
#
# Переменная PATH — это системная переменная, которую операционная система использует для того, чтобы найти нужные исполняемые объекты в командной строке или окне терминала.
#
# env - просмотр списка переменных среды
#
# Слева от знака равенства (=) указывается имя переменной среды, а справа — строковое значение.
#
# export PATH=/newFolder:$PATH - чтобы добавить новые папки в переменную path нужно изменить текстовый файл  .zshrc в домашней папке, добавив в него данную строку
#
# # 3 Глава. Форматирование кода при помощи black.
#
# PEP8 - сводка правил написания кода python, по нему и работает black
#
# ### Использование пробелов для создания отступов
#
# Что лучше - табуляция или пробел?
#
# >>> print('Hello there, friend!\nHow are you?')
# Hello there, friend!
# How are you?
# >>> print('Hello\tthere,\tfriend!\nHow\tare\tyou?')
# Hello   there,  friend!
# How     are     you?
#
# Пробел всегда выводится на
# экран как строковое значение, состоящее из одного пробела —
# ' '. А символ табуляции, который выводится как строковое значение, содержащее служебный символ
# '\t', не столь однозначен. Символы табуляции часто (хотя и не всегда) выводятся
# как переменное количество пробелов, чтобы текст начинался со следующей позиции
# табуляции. Лучше выбрать пробел.
#
# Также не следует смешивать пробелы и символы табуляции для создания отступов в одном блоке кода. Использование обоих символов настолько часто становилось причиной коварных ошибок в более ранних программах Python, что в Python 3 код с такими отступами даже не выполняется — выдается исключение TabError: inconsistent use of tabs and spaces in indentation
#
# Что касается длины каждого уровня отступов, в Python один уровень обычно обо-
# значен четырьмя пробелами.
#
# Также стоит отделять операторы от идентификаторов одним пробелом
#
# Ставьте два пробела перед комментариями в конце строки
#
# print('Hello, world!')  # Вывод приветствия.
#
# Пример правильного использования вертикальных отступов:
#
# class ExampleClass:
#
#     def exampleMethod1():
#         pass
#
#     def exampleMethod2():
#         pass
#
# def exampleFunction():
#         pass
#
# Python предоставляет одну возможность, о которой знают не все: точка с запятой
# (;) может использоваться для разделения нескольких команд в одной строке
#
# print('What is your name?'); name = input()
#
# if name == 'Alice': print('Hello, Alice!')
#
# Обычно такое написание затрудняет читаемость команд, так что  Black разбивает такие команды на отдельные строки.
#
# Аналогичным образом можно импортировать несколько модулей одной командой:
#
# import:
#
# import math, os, sys
#
# Тем не менее PEP 8 рекомендует разбить эту команду на несколько коротких команд, по одной для каждого модуля:
# import math
# import os
# import sys
#
# PEP8 также рекомендует объединять команды import в следующие три группы
# в указанном порядке.
# 1. Модули стандартной библиотеки Python: math, os, sys и т. д.
# 2. Сторонние модули: Selenium, Requests, Django и т. д.
# 3. Локальные модули, являющиеся частью программы.
#
# ## Black
#
# Black автоматически форматирует код в ваших файлах .py.
#
# Его название (Black — черный) происходит от знаменитого высказывания
# Генри Форда относительно цветов выпускаемых автомобилей: «Цвет автомобиля
# может быть любым, при условии что он черный».
#
# ### Предварительный просмотр изменений, вносимых Black
#
# C:\Users\Al>python -m black --diff yourScript.py
#
# Например, если yourScript.py
# содержит строку weights=[42.0,3.1415,2.718], при выполнении с ключом --diff
# будет выведен следующий результат:
# C:\Users\Al\>python -m black --diff yourScript.py
# --- yourScript.py 2020-12-07 02:04:23.141417 +0000
# +++ yourScript.py 2020-12-07 02:08:13.893578 +0000
# @@ -1 +1,2 @@
# -weights=[42.0,3.1415,2.718]
# +weights = [42.0, 3.1415, 2.718]
#
#
# Знак «минус» означает, что Black удалит строку weights=[42.0,3.1415,2.718] и заменит ее строкой, которая выводится с префиксом «плюс»: weights = [42.0, 3.1415, 2.718].
#
# ### Отключение Black для отдельных частей кода
#
# Добавив комментарии # fmt: off и # fmt: on, можно запретить Black форматирование
# строк в этом фрагменте, а затем продолжить его:
#
# ####### Константы для разных промежутков времени:
#
# ####### fmt: off
#
# SECONDS_PER_MINUTE = 60
#
# SECONDS_PER_HOUR = 60 * SECONDS_PER_MINUTE
#
# SECONDS_PER_DAY = 24 * SECONDS_PER_HOUR
#
# SECONDS_PER_WEEK = 7 * SECONDS_PER_DAY
#
# ####### fmt: on
#
# # Глава 4. Выбор понятных имён.
#
# Змеиный регистр (snake_case) разделяет слова символом подчеркивания,
# который напоминает ползущую между словами змею. В этом случае все
# буквы записываются в нижнем регистре, а константы часто записываются
#
# в верхнем змеином регистре (UPPER_SNAKE_CASE).
# Верблюжий регистр (camelCase) — слова записываются в нижнем регистре,
# но второе и следующие слова начинаются с заглавной. Эта схема в большинстве
# случаев подразумевает, что первое слово начинается с буквы нижнего
# регистра. Буквы верхнего регистра напоминают верблюжьи горбы.
#
# Схема Pascal (PascalCase) — названа так, потому что применяется в языке
# программирования Pascal; аналогична схеме верблюжьего регистра, но первое
# слово в ней тоже начинается с заглавной.
#
# **Сводка правил из PEP 8 по переменным:**
#
# - Все буквы должны быть буквами ASCII — то есть латинскими буквами
# верхнего и нижнего регистров без диакритических знаков.
#
# - Имена модулей должны быть короткими и состоять только из букв нижнего
# регистра.
#
# - Имена классов необходимо записывать в схеме Pascal.
#
# - Имена констант следует записывать в верхнем змеином регистре.
#
# - Имена функций, методов и переменных записывают в нижнем змеином
# регистре.
#
# - Первый аргумент методов всегда должен называться self в нижнем регистре.
#
# - Первый аргумент методов классов всегда должен называться cls в нижнем
# регистре.
#
# - Приватные атрибуты классов всегда начинают с символа подчеркивания ( _ ).
# - Публичные атрибуты классов никогда не начинают с символа подчеркивания ( _ ).
#
# Выбирайте имена, пригодные для поиска (закладывайте уникальность)
#
# Не заменяйте встроенные имена
#
# # Глава 5. Поиск запахов в коде.(Что может стать причиной ошибки?)
#
# Самый распространенный источник ошибок — ***дублирование кода.***
#
# Проблема решается функцией или циклом
#
# ***Закомментированный и мертвый код***
#
# Мертвым называется код, который недоступен или никогда не может быть выполнен на логическом уровне.
#
# ***Переменные с числовыми суффиксами***
#
# Пример - num1 num2 num 3 num4
#
# Если количество числовых суффиксов больше двух, стоит подумать об использовании структур: списка или множества для хранения данных в виде коллекции.
#
# ***Классы, которые должны быть функциями или модулями***
#
# Не стоит закладывать в класс функцию, которую можно заменить на простой вызов встроенной/пользовательской функции.
#
# ***Списковые включения внутри списковых включений***
#
# Вложенные списковые включения (или вложенные включения множеств/
# словарные включения) упаковывают значительную сложность в небольшой объем
# кода, что усложняет его чтение. Лучше развернуть списковое включение в один
# или несколько циклов for
#
# ***Пустые блоки except и плохие сообщения об ошибках***
#
#
# # Глава 6. Написание питонического кода.
#
# «Дзен Python» — набор из 20 руководящих принципов проектирования языка
# Python и программ Python, написанный Тимом Петерсом.
#
# The Zen of Python, by Tim Peters
#
# Beautiful is better than ugly.
#
# Explicit is better than implicit.
#
# Simple is better than complex.
#
# Complex is better than complicated.
#
# Flat is better than nested.
#
# Sparse is better than dense.
#
# Readability counts.
#
# Special cases aren't special enough to break the rules.
#
# Although practicality beats purity.
#
# Errors should never pass silently.
#
# Unless explicitly silenced.
#
# In the face of ambiguity, refuse the temptation to guess.
#
# There should be one-- and preferably only one --obvious way to do it.
#
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
#
# Although never is often better than *right* now.
#
# If the implementation is hard to explain, it's a bad idea.
#
# If the implementation is easy to explain, it may be a good idea.
#
# Namespaces are one honking great idea -- let's do more of those!
#
#
# Правило: сначала заставьте свой код работать, а потом
# переходите к оптимизации. Когда у вас уже имеется работоспособная программа,
# тогда и стоит браться за повышение ее эффективности.
#
# Стоит использовать:
#
#   - enumerate вместо range(len())
#
#   - with вместо open() и close()
#
#   - is для сравнения с None вместо ==
#
#   - необработанную строку (raw), если строка содержит много символов \
#
#   - Форматирование с использованием F-строк
#
#   - get() и setdefault() со словарями:
#
#         Вызов numberOfPets.get('cats', 0) проверяет, существует ли ключ 'cats' в словаре numberOfPets. Если он существует, то вызов метода возвращает значение для
#         ключа 'cats'. Если ключ не существует, вместо значения возвращается второй
#         аргумент 0. Использование метода get() с определением значения по умолчанию,
#         которое должно использоваться для несуществующих ключей, короче и лучше
#         читается, чем решение с командами if-else.
#
#
#         numberOfPets.setdefault('cats', 0) # Ничего не делать, если 'cats' существует.
#
#   - collections.defaultdict для значений по умолчанию:
#
#         >>> import collections
#         >>> scores = collections.defaultdict(int)
#         >>> scores
#         defaultdict(<class 'int'>, {})
#         >>> scores['Al'] += 1 # Не нужно сначала задавать значение для ключа 'Al'.
#         >>> scores
#         defaultdict(<class 'int'>, {'Al': 1})
#         >>> scores['Zophie'] # Не нужно сначала задавать значение для ключа 'Zophie'.
#         0
#         >>> scores['Zophie'] += 40
#         >>> scores
#         defaultdict(<class 'int'>, {'Al': 1, 'Zophie': 40})
#
#   - словари вместо многократных if-elif-else
#
#
# ### Проверка того, что переменная содержит одно из нескольких значений
#
#     >>> # Пример питонического кода.
#     >>> spam = 'cat'
#     >>> spam in ('cat', 'dog', 'moose')
#     True
#
#
# # Глава 7. Жаргон программистов
#
# В Python существует сборка мусора (garbage
# collection) — механизм автоматического управления памятью, который отслеживает выделение и освобождение памяти, чтобы программисту не приходилось заниматься этим самому.
#
# Литерал (literal) — текст в исходном коде программы, определяющий фиксированное типизованное значение.
#
# True, False и None считаются ключевыми словами Python, а не литералами, тогда как [] и {} называются
# индикаторами (displays) или атомами (atoms)
#
# Знаки мат операций, is, not, равенство и тд называются операторами
#
# Объект (object) представляет некоторый фрагмент данных: число, текст или более
# сложную структуру данных (такую как список или словарь). Все объекты могут
# сохраняться в переменных, передаваться в аргументах при вызове функций и возвращаться из вызовов функций.
# Каждый объект характеризуется значением, идентичностью и типом данных (value,
# identity и data type).
#
# Значение — данные, представляемые объектом
#
# идентичность — уникальное целое число, которое можно
# просмотреть вызовом функции id().
#
# Элемент - объект находящийся в объекте контейнере
#
# Последовательность (sequence) представляет собой объект любого контейнерного
# типа данных с упорядоченными значениями, к которым можно обращаться по
# целым индексам.
#
# Отображение (mapping) представляет собой объект любого контейнерного типа
# данных, использующий ключи вместо индексов.
#
# Dunder-методы, называемые также магическими, — это специальные методы
# в Python, которые используются для перезагрузки операторов. Их имена начинают-
# ся и заканчиваются двумя символами подчеркивания ( __ ).
#
# Модуль - импортируемый сборник программ Python
# Пакет - набор модулей
#
# Вызываемые объекты - объекты, реализующие оператор вызова ()
#
# Первоклассные объекты - объекты, которые можно присваивать, передавать в функции, возвращать.
#
# Выражениями (expressions) называются инструкции, состоящие из операторов и значений, результатом вычисления которых является одно значение.
#
# Блок, секция, тело - фрагмент кода, обрамленный отступами и обремененный одной целью
#
# Переменные (variables) — имена, ссылающиеся на объекты.
#
# Атрибут - любое имя, следующее за точкой
#
# Откомпилированная программа, состоящая из машинного кода,
# называется двоичным файлом
#
# Байт-код, также называемый портируемым (portable) кодом, или p-кодом, является аналогом машинного кода, но выполняется не напрямую процессором, а специальной программой — интерпретатором.
#
# Библиотека (library) — общий термин для подборки кодов, написанных третьей
# стороной.
#
# Фреймворком (framework) называется подборка кода, работающая по принципу
# инверсии управления; разработчик пишет функции, которые вызываются фреймворком по мере надобности
#
# SDK (Software Development Kit — комплект разработки ПО) — это программные
# библиотеки, документация и программные средства, упрощающие создание приложений для конкретной операционной системы или платформы.
#
# Ядро, или движок (engine), — крупная автономная система, которой могут управлять внешние программы разработчика.
#
# Интерфейс прикладного программирования, или API (Application Programming
# Interface), — интерфейс для работы с библиотекой, SDK, фреймворком или ядром,
# предназначенный для внешнего использования.
#
# # Глава 8. Часто встречающиеся ловушки Python
#
# Не добавляйте и не удаляйте элементы из списка
# в процессе перебора - вероятность столкнуться с бесконечным циклом очень высока.
#
# Также не стоит удалять элементы итерируемого списка в процессе цикла, так как смещения по индексам может привести к неверному результату.
#
# Python никогда не копирует объекты, он копирует только ссылки на них, так что при изменении первоначального объекта, изменяется последующие объекты, связанные со значением первоначального. Это можно решить поверхностным копированием объекта: copy.copy().
#
# Не используйте изменяемые значения для аргументов по умолчанию

#