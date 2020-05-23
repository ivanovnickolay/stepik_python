# Вася решил открыть АЗС (заправку). Чтобы оценить уровень конкуренции он хочет изучить
# количество заправок в интересующем его районе. Вася скачал интересующий его кусок карты OSM
# https://stepik.org/media/attachments/lesson/245681/map2.osm и хочет посчитать, сколько на нём
# отмечено точечных объектов (node), являющихся заправкой. В качестве ответа вам необходимо
# вывести одно число - количество АЗС.
#
# "Как обозначается заправка в OpenStreetMap" - пример хорошего запроса чтобы узнать,
# как обозначается заправка в OpenStreetMap.
# "amenity=fuel"

import xmltodict

fin = open('map2.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()

parsedxml = xmltodict.parse(xml)
cnt_fuel = 0

for node in parsedxml['osm']['node']:
    if 'tag' in node:
        tags = node['tag']
        if isinstance(tags, list):
            for tag in tags:
                if '@k' in tag and tag['@k'] == 'amenity' and tag['@v'] == 'fuel':
                    cnt_fuel += 1
        else:
            if '@k' in tags and tags['@k'] == 'amenity' and tags['@v'] == 'fuel':
                cnt_fuel += 1
print(cnt_fuel)