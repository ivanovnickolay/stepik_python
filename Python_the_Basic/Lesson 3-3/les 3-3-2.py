# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве слова.

# Sample Input:
#
# cat
# catapult and cat
# catcat
# concat
# Cat
# "cat"
# !cat?
# Sample Output:
#
# cat
# catapult and cat
# "cat"
# !cat?

import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    regex = r"\b(cat)\b"
    matches = re.findall(regex, line, re.MULTILINE)
    if len(matches) != 0:
        print(line)
