# Мы сохранили страницу с википедии про языки программирования и сохранили по адресу
# https://stepik.org/media/attachments/lesson/209717/1.html
#
# Скачайте её с помощью скрипта на Питоне и посчитайте, какой язык упоминается чаще
# Python или C++ (ответ должен быть одной из этих двух строк).

import requests

r = requests.get('https://stepik.org/media/attachments/lesson/209717/1.html')
cnt_python = r.text.count('Python')
cnt_cpp = r.text.count('C++')
if cnt_cpp > cnt_python:
    print('C++')
else:
    print('Python')
