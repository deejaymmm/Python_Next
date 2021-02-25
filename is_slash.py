import re
import sys
pattern = r".*\\.*"
for line in sys.stdin:
    string = line.rstrip()
    if len(re.findall(pattern, string)) > 0:
        print(string)

"""
Вам дана последовательность строк.
Выведите строки, содержащие обратный слеш "\".
Sample Input:

\w denotes word character
No slashes here
Sample Output:

\w denotes word character
"""