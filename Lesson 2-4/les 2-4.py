import os
list_path_py = []
# list_dir = os.walk('main')
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        if name.endswith(".py"):
            if os.path.join(root) not in list_path_py:
                list_path_py.append(os.path.join(root))
list_path_py.sort()
for d in list_path_py:
    print(d[2:])
