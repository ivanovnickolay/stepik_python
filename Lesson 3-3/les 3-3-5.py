# Вам дана последовательность строк.
# Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).
#
# Sample Input:
#
# blabla is a tandem repetition
# 123123 is good too
# go go
# aaa
# Sample Output:
#
# blabla is a tandem repetition
# 123123 is good too

import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    # regex = r"\b(\w+)(\w+)?\w?\2?\1\b"
    regex = r'\b(.+)\1\b'
    matches = re.findall(regex, line, re.MULTILINE)
    if len(matches) != 0:
        print(line)