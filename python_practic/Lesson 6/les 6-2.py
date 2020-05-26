# В этой задаче вам необходимо научиться генерировать html-код на питоне и сдать на проверку html-файл,
# в котором будет таблица размером 10 на 10, которая должна содержать таблицу умножения для
# чисел от 1 до 10. При открытии вашего файла в браузере это должно выглядеть примерно так
#
# Ваш файл должен начинаться с тегов <html> и <body> и заканчиваться </body> и </html>.
#
# Для создания таблицы можно пользоваться тегами <table> (создание таблицы),
# <tr> (создание строки в таблице) и <td> (создание отдельной ячейки). Все открытые теги нужно закрыть,
# причем сделать это нужно в правильном порядке.
#
# Пожалуйста, не используйте никаких украшений и других тегов - мы не сможем проверить
# такие решения.

table = '<table>'
for x in range(1, 11):
    table = table + '<tr>'
    for y in range(1, 11):
        table = table +'<td>' + str(x * y) + '</td>'
    table = table + '</tr>'
table = table + '</table>'

with open('les 6-2.html', 'x') as f:
    f.write('<html> <body>')
    f.write(table)
    f.write('</body></html>')