string = input().strip()
str_from = input().strip()
str_to = input().strip()
num_occur = 0
while True:
    cur_str = string.replace(str_from, str_to)
    if num_occur > 1000 \
            or (str_from in str_to and str_from in string) \
            or len(cur_str) > len(string):
                # Если не проверить последнее условие,
                # начинаются "чудеса" (Memory Overflow)
        print('Impossible')
        break
    elif string == cur_str:
        print(num_occur)
        break
    else:
        string = cur_str
        num_occur += 1
"""
Вашей программе на вход подаются три строки s, a, b, состоящие из строчных 
латинских букв.
За одну операцию вы можете заменить все вхождения строки a в строку s 
на строку b.

Например, s = "abab", a = "ab", b = "ba", тогда после выполнения одной 
операции строка s перейдет в строку "baba", после выполнения двух и операций – 
в строку "bbaa", и дальнейшие операции не будут изменять строку s.

Необходимо узнать, после какого минимального количества операций в строке s 
не останется вхождений строки a. Если операций потребуется более 1000, выведите 
Impossible.

Выведите одно число – минимальное число операций, после применения которых 
в строке s не останется вхождений строки a, или Impossible, если операций 
потребуется более 1000.

Условие задачи было изменено 12.09.2018
Sample Input 1:

ababa
a
b
Sample Output 1:

1
Sample Input 2:

ababa
b
a
Sample Output 2:

1
Sample Input 3:

ababa
c
c
Sample Output 3:

0
Sample Input 4:

ababac
c
c
Sample Output 4:

Impossible
"""

