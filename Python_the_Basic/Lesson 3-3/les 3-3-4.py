# Вам дана последовательность строк.
# Выведите строки, содержащие обратный слеш "\﻿".
# Sample Input:
#
# \w denotes word character
# No slashes here
# Sample Output:
#
# \w denotes word character


import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    regex = r"\\"
    matches = re.findall(regex, line, re.MULTILINE)
    if len(matches) != 0:
        print(line)
