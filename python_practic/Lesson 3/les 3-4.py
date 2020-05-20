# Васю назначили завхозом в туристической группе и он подошёл к подготовке ответственно,
# составив справочник продуктов с указанием калорийности на 100 грамм, а также содержание
# белков, жиров и углеводов на 100 грамм продукта. Ему не удалось найти всю информацию,
# поэтому некоторые ячейки остались незаполненными (можно считать их значение равным нулю).
# Также он использовал какой-то странный офисный пакет и разделял целую и дробную часть чисел запятой.
# Таблица доступна по ссылке https://stepik.org/media/attachments/lesson/245290/trekking2.xlsx
#
# Вася составил раскладку по продуктам на один день (она на листе "Раскладка")
# с указанием названия продукта и его количества в граммах. Посчитайте 4 числа: суммарную калорийность и
# граммы белков, жиров и углеводов. Числа округлите до целых вниз и введите через пробел.

import xlrd
import math as m

wb = xlrd.open_workbook('trekking2.xlsx')
sheet_names = wb.sheet_names()
sh = wb.sheet_by_name(sheet_names[0])
products = {}

for row_num in range(1, sh.nrows):
    product: str = (sh.row_values(row_num, 0, 1))[0]
    caloriya: str = str((sh.row_values(row_num, 1, 2))[0]).replace(',', '.')
    protein : str = str((sh.row_values(row_num, 2, 3))[0]).replace(',', '.')
    jir : str = str((sh.row_values(row_num, 3, 4))[0]).replace(',', '.')
    uglevod : str = str((sh.row_values(row_num, 4, 5))[0]).replace(',', '.')
    if protein =='':
       protein = '0'
    if jir == '':
       jir = '0'
    if uglevod == '':
       uglevod = '0'

    products[product] = {'caloriya' : caloriya, 'protein' : protein, 'jir' : jir, 'uglevod' : uglevod}

sh2 = wb.sheet_by_name(sheet_names[1])
sum_caloriya = 0
sum_protein = 0
sum_jir = 0
sum_uglevod = 0
for row_num in range(1, sh2.nrows):
    product_menu: str = (sh2.row_values(row_num, 0, 1))[0]
    ves: str = str((sh2.row_values(row_num, 1, 2))[0]).replace(',', '.')
    sum_caloriya += float(products[product_menu]['caloriya']) * (float(ves) / 100)
    sum_protein += float(products[product_menu]['protein']) * (float(ves) / 100)
    sum_jir += float(products[product_menu]['jir']) * (float(ves) / 100)
    sum_uglevod += float(products[product_menu]['uglevod']) * (float(ves) / 100)


print(round(sum_caloriya, 2), round(sum_protein, 2), round(sum_jir, 2), round(sum_uglevod,2))
print(m.floor(sum_caloriya), m.floor(sum_protein), m.floor(sum_jir), m.floor(sum_uglevod))
