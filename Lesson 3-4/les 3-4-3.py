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


def is_port(url: str) -> str:
    d = url.split(":")
    return d[0]

def is_not_links(url:str)->bool:
    if url.endswith('css'):
        return False
    if url.endswith('js'):
        return False
    return True

protocols = ['http:', 'https:', 'ftp:']
control_links = set()
link_1 = input()
res_1 = requests.get(link_1)
text_res = res_1.text
# получаем все линки по первой ссылке
link_temp = re.findall(r'href=[\'"]?([^\'" >]+)', text_res)
# link_temp = re.findall(r'<a[\s|\S].*? href=[\'"]?([^\'" >]+)', text_res)
# по очереди обходим их
for l in link_temp:
    if is_not_links(l):
        f = l.split('/')
        # если указан протокол
        if f[0] in protocols:
            control_links.add(is_port(f[2]))
            # print(l + " -> " + is_port(f[2]))
            continue
        # если указан пути типа "../skip_relative_links'
        if f[0] == '..':
            continue
        else:
            control_links.add(is_port(f[0]))
            # print(l + " -> " + is_port(f[0]))

links = list(control_links)
links.sort()
for c in links:
    print(c)
