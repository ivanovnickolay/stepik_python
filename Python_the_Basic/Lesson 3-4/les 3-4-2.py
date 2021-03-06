# Рассмотрим два HTML-документа A и B.
# Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, возможно с дополнительными параметрами внутри тега.
# Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход и из C в B можно перейти за один переход.
#
# Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
# Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.
#
# Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.

import requests
import re

control_links = []
link_1 = input()
link_2 = input()
res_1 = requests.get(link_1)
text_res = res_1.text
# получаем все линки по первой ссылке
link_temp = re.findall(r'href=[\'"]?([^\'" >]+)', text_res)
# по очереди обходим их
for l in link_temp:
    res_2 = requests.get(l)
    # если ссылка существует
    if res_2.status_code == 200:
        # получаем все ссылки с страницы
        t = re.findall(r'href=[\'"]?([^\'" >]+)', res_2.text)
        control_links.extend(t)

if link_2 in control_links:
    print("Yes")
else:
    print("No")
