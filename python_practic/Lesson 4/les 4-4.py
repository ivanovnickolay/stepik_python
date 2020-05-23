# Вася, открывший заправку в прошлом уроке, разорился. Конкуренция оказалась
# слишком большой. Вася предполагает, что это произошло от того, что теги
# заправки могут быть не только на точке, но и на каком-то контуре. Определите,
# сколько заправок на самом деле (не только обозначенных точкой) есть на фрагменте карты
# https://stepik.org/media/attachments/lesson/245681/map2.osm

import xmltodict

fin = open('map3.osm', 'r', encoding='utf8')
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

for node in parsedxml['osm']['way']:
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