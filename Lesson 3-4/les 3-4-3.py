# Вашей программе на вход подается ссылка на HTML файл.
# Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и вывести список сайтов, на которые есть ссылка.
#
# Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это последовательность символов, которая следует сразу после символов протокола, если он есть, до символов порта или пути, если они есть, за исключением случаев с относительными ссылками вида
# <a href="../some_path/index.html">.
#
# Сайты следует выводить в алфавитном порядке.
#
# Пример HTML файла:
#
# <a href="http://stepic.org/courses">
# <a href='https://stepic.org'>
# <a href='http://neerc.ifmo.ru:1345'>
# <a href="ftp://mail.ru/distib" >
# <a href="ya.ru">
# <a href="www.ya.ru">
# <a href="../skip_relative_links">
#
# Пример ответа:
#
# mail.ru
# neerc.ifmo.ru
# stepic.org
# www.ya.ru
# ya.ru
import requests
import re

control_links = set()
link_1 = input()
res_1 = requests.get(link_1)
text_res = res_1.text
# получаем все линки по первой ссылке
link_temp = re.findall(r'href=[\'"]?([^\'" >]+)', text_res)
# по очереди обходим их
for l in link_temp:
    f = l.split('/')
    control_links.add(f[2])
    # if f[2] not in control_links:
    #     control_links.append(f[2])
    print(l + " -> " + f[2])
    # res_2 = requests.get(l)
    # print(l)
    # # если ссылка существует
    # if res_2.status_code == 200:
    #     # получаем все ссылки с страницы

links = list(control_links)
links.sort()
for c in links:
    print(c)