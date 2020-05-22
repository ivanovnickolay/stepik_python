# Главный бухгалтер компании "Рога и копыта" случайно удалил ведомость с начисленной зарплатой.
# К счастью, у него сохранились расчётные листки всех сотрудников. Помогите по этим расчётным
# листкам восстановить зарплатную ведомость. Архив с расчётными листками доступен по ссылке
# https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip (вы можете скачать и распаковать
# его вручную или самостоятельно научиться делать это с помощью скрипта на Питоне).
#
# Ведомость должна содержать 1000 строк, в каждой строке должно быть указано ФИО сотрудника и, через пробел, его зарплата.
# Сотрудники должны быть упорядочены по алфавиту.
import xlrd
import os
list_files = os.listdir('rogaikopyta')
salary_by_name = {}
for file in list_files:
    path = os.getcwd() + '//rogaikopyta//' + file
    if os.access(path, os.R_OK):
        wb = xlrd.open_workbook(path)
        sheet_names = wb.sheet_names()
        sh = wb.sheet_by_name(sheet_names[0])
        name: str = (sh.row_values(1, 1, 2))[0]
        salary = int((sh.row_values(1, 3, 4))[0])
        salary_by_name[name] = salary

keys = sorted(list(salary_by_name.keys()))

for name in keys:
    print(name, salary_by_name[name])

