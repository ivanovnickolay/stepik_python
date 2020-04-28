# Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года
# по настоящее время.
#
# Одним из атрибутов преступления является его тип – Primary Type.
#
# Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

import csv

Primary_Type = {}
with open('Crimes.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[5] in Primary_Type.keys():
            Primary_Type[row[5]] = Primary_Type[row[5]] + 1
        else:
            Primary_Type[row[5]] = 1
print(Primary_Type)
sorted_by_value = sorted(Primary_Type.items(), key=lambda kv: kv[1])
print(sorted_by_value[-1])