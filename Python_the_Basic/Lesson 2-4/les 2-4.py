#
# Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.
#
# Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории, в которых есть хотя бы один файл с расширением ".py".
#
# Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.

import os
list_path_py = []
# list_dir = os.walk('main')
for root, dirs, files in os.walk("", topdown=False):
    for name in files:
        if name.endswith(".py"):
            if os.path.join(root) not in list_path_py:
                list_path_py.append(os.path.join(root))
list_path_py.sort()
for d in list_path_py:
    print(d[2:])
