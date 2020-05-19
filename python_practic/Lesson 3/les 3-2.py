# Вася планирует карьеру и переезд. Для это составил таблицу, в которой для каждого региона
# записал зарплаты для разных интересные ему профессий. Таблица доступна по ссылке
# https://stepik.org/media/attachments/lesson/245267/salaries.xlsx. Выведите название региона
# с самой высокой медианной зарплатой (медианой называется элемент, стоящий в середине массива
# после его упорядочивания) и, через пробел, название профессии с самой высокой средней зарплатой по всем регионам.


import xlrd
import statistics as st

wb = xlrd.open_workbook('salaries.xlsx')
sheet_names = wb.sheet_names()
sh = wb.sheet_by_name(sheet_names[0])
list_position = {}
list_town = {}
max_mediana = 0

for row_num in range(1, sh.nrows):
    salary = sh.row_values(row_num,1)
    median_salary_town = st.median(sorted(salary))

    if median_salary_town > max_mediana:
        max_mediana = median_salary_town
        town = sh.row_values(row_num, 0, 1)

cnt = 0
cnt_list_row = len(sh.row_values(row_num,0))
max_mean = 0
position = ''
for f in range(1,cnt_list_row):
    col_val = sh.col_values(f,1)
    av_col = st.mean(col_val)
    if av_col > max_mean :
        max_mean = av_col

        position = (sh.col_values(f, 0))[0]


print(town[0])
print(max_mediana)
print(position)
print(str(max_mean))