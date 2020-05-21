# Васю назначили завхозом в туристической группе и он подошёл к подготовке ответственно,
# составив справочник продуктов с указанием калорийности на 100 грамм, а также содержание белков,
# жиров и углеводов на 100 грамм продукта. Ему не удалось найти всю информацию, поэтому некоторые
# ячейки остались незаполненными (можно считать их значение равным нулю).
# Также он использовал какой-то странный офисный пакет и разделял целую и дробную часть чисел запятой. Таблица доступна по ссылке https://stepik.org/media/attachments/lesson/245290/trekking3.xlsx
#
# Вася составил раскладку по продуктам на весь поход (она на листе "Раскладка")
# с указанием номера дня, названия продукта и его количества в граммах.
# Для каждого дня посчитайте 4 числа: суммарную калорийность и граммы белков, жиров и углеводов.
# Числа округлите до целых вниз и введите через пробел. Информация о каждом дне должна выводиться в отдельной строке.

import xlrd
import math as m

wb = xlrd.open_workbook('trekking3.xlsx')
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
day_racion = {}
for row_num in range(1, sh2.nrows):
    sum_caloriya = 0
    sum_protein = 0
    sum_jir = 0
    sum_uglevod = 0
    day: str = (sh2.row_values(row_num, 0, 1))[0]
    product_menu: str = (sh2.row_values(row_num, 1, 2))[0]
    ves: str = str((sh2.row_values(row_num, 2, 3))[0]).replace(',', '.')
    sum_caloriya = float(products[product_menu]['caloriya']) * (float(ves) / 100)
    sum_protein = float(products[product_menu]['protein']) * (float(ves) / 100)
    sum_jir = float(products[product_menu]['jir']) * (float(ves) / 100)
    sum_uglevod = float(products[product_menu]['uglevod']) * (float(ves) / 100)
    if day in day_racion:
        day_racion[day]['caloriya'] += sum_caloriya
        day_racion[day]['protein'] += sum_protein
        day_racion[day]['jir'] += sum_jir
        day_racion[day]['uglevod'] += sum_uglevod
    else:
        day_racion[day] = {'caloriya' : sum_caloriya, 'protein' : sum_protein, 'jir' : sum_jir, 'uglevod' : sum_uglevod}

for day in day_racion.keys():
    # print(round(day_racion[day]['caloriya'], 2), round(day_racion[day]['protein'], 2), round( day_racion[day]['jir'], 2), round(day_racion[day]['uglevod'],2))
    print(m.floor(day_racion[day]['caloriya']), m.floor(day_racion[day]['protein']), m.floor(day_racion[day]['jir']), m.floor(day_racion[day]['uglevod']))