# В OpenStreetMap XML встречаются теги node, которые соответствуют некоторым точкам на карте.
# Ноды могут не только обозначать какой-то точечный объект, но и входить в состав way
# (некоторой линии, возможно замкнутой) и не иметь собственных тегов.
# Для доступного по ссылке https://stepik.org/media/attachments/lesson/245678/map1.osm фрагмента карты
# посчитайте, сколько node имеет хотя бы один вложенный тэг tag, а сколько - не имеют.
# В качестве ответа введите два числа, разделённых пробелом.
import xmltodict

fin = open('map1.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()

parsedxml = xmltodict.parse(xml)
cnt_tag = 0
cnt_no_tag = 0

for node in parsedxml['osm']['node']:
    if 'tag' in node:
        cnt_tag += 1
    else:
        cnt_no_tag += 1

print(cnt_tag, cnt_no_tag)