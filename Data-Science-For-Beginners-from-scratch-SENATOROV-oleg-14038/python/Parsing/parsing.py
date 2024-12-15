# +
"""This module is designed for web scraping and data extraction tasks.

It uses the requests library to fetch web pages. BeautifulSoup to parse. and
extract meaningful data from HTML content.
"""

import requests
from bs4 import BeautifulSoup

# Your web scraping code here...

# +
# def get_html(url): # функция который шлет запрос на сервер и
#     r = requests.get(url) # get метод запроса который отправляется на сервер
# #     type(r) # Тип данных Response
# #     dir(r) # Показывает атрибуты обекта
# #     r.text # получаем текст html
# #     r.status_code # ответ статус код 200, 403 - доступ заприщен
#     return r.text, r.status_code

# +
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     h1 = soup.find('div', id='home-welcome').find('header').find('h1').text
#     return h1

# +
# def main():
#     url = "https://ru.wordpress.org"
#     print(get_data(get_html(url))) # type: ignore

# +
# if __name__ == "__main__":
#     main()
# -


def get_html(url_one: str) -> tuple[str, int]:
    """Получает HTML-код страницы по заданному URL.

    Возвращает текст ответа и код статуса.

    Параметры.
    url (str): URL-адрес страницы, HTML-код которой необходимо получить.

    Возвращает.
    tuple[str, int]: Кортеж, содержащий.
        - HTML-код страницы (str).
        - Код статуса HTTP-ответа (int).
    """
    req = requests.get(url_one)
    return req.text, req.status_code


def get_data(html: str) -> str:
    """Извлекает текст заголовка из HTML-кода страницы.

    с использованием BeautifulSoup.

    Параметры.
    html (str): Строка, содержащая HTML-код страницы, из.
    которого необходимо извлечь заголовок.

    Возвращает.
    str: Текст заголовка из элемента <h1> внутри <header>.
    с id="home-welcome".

    Исключения.
    Если элемент с id="home-welcome" или его дочерние.
    элементы не найдены, функция может вызвать AttributeError.
    """
    soup = BeautifulSoup(html, "lxml")
    header_text = soup.find("div", id="home-welcome").find("header").find("h1").text
    return str(header_text)


# +
def main() -> None:
    """Основная функция программы. Выполняет следующие действия.

    1. Устанавливает URL-адрес веб-страницы.
    2. Получает HTML-код страницы по заданному URL
       с помощью функции `get_html`.
    3. Извлекает и выводит заголовок из HTML-кода
       страницы с помощью функции `get_data`.

    Параметры:
    Нет параметров.

    Возвращает:
    Нет возвращаемого значения.

    Исключения:
    - Возможные исключения, возникшие при выполнении
      `get_html` или `get_data`, не обрабатываются в этой функции.
    - Может вызвать исключения сетевого запроса или
      ошибки обработки HTML, если URL недоступен или
      структура HTML неожиданная.
    """


url_one_line = "https://wordpress.org/"


html_content = get_html(url_one_line)[0]
# Extract only the string from the tuple
get_data(html_content)
# -

if __name__ == "__main__":
    main()
