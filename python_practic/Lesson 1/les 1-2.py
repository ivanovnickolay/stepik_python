# Файл https://stepik.org/media/attachments/lesson/209719/2.html
# содержит статью с Википедии про язык Python. В этой статье есть теги code,
# которыми выделяются конструкции на языке Python. Вам нужно найти все строки,
# содержащиеся между тегами <code> и </code> и найти те строки, которые встречаются чаще всего и
# вывести их в алфавитном порядке, разделяя пробелами.
#
# Например, если исходный текст страницы выглядел бы так:
#
# <code>a</code>
# <a>bracadabr</a>
# <code>c</code>
# <code>b</code>
# <code>b</code>
# <code>c</code>
# то в ответ надо было бы ввести строку "b c".

import requests
from collections import Counter

r = requests.get('https://stepik.org/media/attachments/lesson/209719/2.html').text

result = {}
index_ = 0
temp = r
while index_ <= len(r):

    begin = temp.find('<code>')
    if begin == -1:
        break
    end = temp.find('</code>')
    tags = temp[begin+6:end]
    if tags in result.keys():
        result[tags] = result[tags] + 1
    else:
        result[tags] = 1
    if (end + 7) < len(r):
        index_ = end + 7
    else:
        break
    temp = temp[index_:]

for k, v in (Counter(result).most_common()):
    print(f'{k}:{v}')
