# Вам дана последовательность строк.
# В каждой строке замените все вхождения подстроки "human" на подстроку "computer"﻿ и выведите полученные строки.
#
# Sample Input:
#
# I need to understand the human mind
# humanity
# Sample Output:
#
# I need to understand the computer mind
# computerity

import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    regex = r'\b(.+)\1\b'
    line_sub = re.sub("human","computer", line)
    print(line_sub)