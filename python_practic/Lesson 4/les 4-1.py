# В этой задаче нужно просто установить библиотеку xmltodict, скачать файл
# https://stepik.org/media/attachments/lesson/245571/map1.osm, создать в директории
# с файлом скрипт со следующим содержанием:
# и ввести в качестве ответа вывод этого скрипта.

import xmltodict

fin = open('map1.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()

parsedxml = xmltodict.parse(xml)
print(parsedxml['osm']['node'][100]['@id'])