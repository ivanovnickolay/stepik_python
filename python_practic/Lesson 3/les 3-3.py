# Васю назначили завхозом в туристической группе и он подошёл к подготовке ответственно,
# составив справочник продуктов с указанием калорийности на 100 грамм, а также содержание
# белков, жиров и углеводов на 100 грамм продукта. Ему не удалось найти всю информацию,
# поэтому некоторые ячейки остались незаполненными (можно считать их значение равным нулю).
# Также он использовал какой-то странный офисный пакет и разделял целую и дробную часть чисел запятой.
# Таблица доступна по ссылке https://stepik.org/media/attachments/lesson/245290/trekking1.xlsx
#
# Вася хочет минимизировать вес продуктов и для этого брать самые калорийные продукты.
# Помогите ему и упорядочите продукты по убыванию калорийности.
# В случае, если продукты имеют одинаковую калорийность - упорядочите их по названию.
# В качестве ответа необходимо сдать названия продуктов, по одному в строке.

import xlrd

wb = xlrd.open_workbook('trekking1.xlsx')
sheet_names = wb.sheet_names()
sh = wb.sheet_by_name(sheet_names[0])
calor = {}

for row_num in range(1, sh.nrows):
    product: str = (sh.row_values(row_num, 0, 1))[0]
    caloriya: str = (sh.row_values(row_num, 1, 2))[0]
    if str(caloriya).find(',') != -1:
        # temp = caloriya
        # del caloriya
        caloriya = caloriya.replace(',', '.')
    if caloriya in calor:
        calor[caloriya].append(product)
    else:
        calor[caloriya] = []
        calor[caloriya].append(product)
key_sort = sorted(list(calor.keys()))
key_sort.reverse()
for h in key_sort:
    products = sorted(calor[h])

    for p in range(len(products)):
        print(products[p])
