# Вам дано описание пирамиды из кубиков в формате XML.
# Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue﻿).
# Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.
#
# Пример:
# <cube color="blue">
#   <cube color="red">
#     <cube color="green">
#     </cube>
#   </cube>
#   <cube color="red">
#   </cube>
# </cube>
# Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1.
# Кубики, расположенные прямо под ним, имеют ценность 2.
# Кубики, расположенные прямо под нижележащими кубиками, имеют ценность 3. И т. д.
#
# Ценность цвета равна сумме ценностей всех кубиков этого цвета.
#
# # Выведите через пробел три числа: ценности красного, зеленого и синего цветов.
#
# Sample Input:
# <cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>
# Sample Output:
# 4 3 1

from xml.etree import ElementTree


def readChildElement(el: ElementTree, level: int):
    if len(el) != 0:
        # cube_res[el.attrib['color']] = cube_res[el.attrib['color']] + level
        for child in el:
            cube_res[child.attrib['color']] = cube_res[child.attrib['color']] + level
            readChildElement(child, level+1)


cube_res = {'blue': 0, 'red': 0, 'green': 0}

str_xml = input()
level_point = 1
root = ElementTree.fromstring(str_xml)
cube_res[root.attrib['color']] = cube_res[root.attrib['color']] + level_point
# обходим первый уровень
readChildElement(root, level_point+1)

print(str(cube_res['red']) + ' ' + str(cube_res['green']) + ' ' + str(cube_res['blue']))
