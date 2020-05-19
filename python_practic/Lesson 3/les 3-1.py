# Для решения этой задачи необходимо установить библиотеку xlrd,
# скачать файл https://stepik.org/media/attachments/lesson/245266/tab.xlsx и создать в папке с
# этим файлом скрипт со следующем содержанием:
#
# import xlrd
#
# wb = xlrd.open_workbook('tab.xlsx')
# sheet_names = wb.sheet_names()
# sh = wb.sheet_by_name(sheet_names[0])
# nmin = sh.row_values(6)[2]
# for rownum in range(7, 27):
#     temp = sh.row_values(rownum)
#     nmin = min(nmin, temp[2])
# print(nmin)
# Запустите скрипт и в качестве ответа введите то, что он выведет.


import xlrd

wb = xlrd.open_workbook('tab.xlsx')
sheet_names = wb.sheet_names()
sh = wb.sheet_by_name(sheet_names[0])
nmin = sh.row_values(6)[2]
for rownum in range(7, 27):
    temp = sh.row_values(rownum)
    nmin = min(nmin, temp[2])
print(nmin)