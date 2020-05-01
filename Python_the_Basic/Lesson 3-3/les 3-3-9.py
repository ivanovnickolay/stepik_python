# Вам дана последовательность строк.
# В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
# Буквой считается символ из группы \w.
# Sample Input:
#
# attraction
# buzzzz
# Sample Output:
#
# atraction
# buz

import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    regex = r"(\w)(\1)+"
    line_sub = re.sub(regex,  r"\1", line)
    print(line_sub)