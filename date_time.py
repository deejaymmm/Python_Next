from datetime import datetime, timedelta

year_month_day = [int(i) for i in input().split(' ')]
num_days = int(input())

origin_date = datetime(year_month_day[0], year_month_day[1], year_month_day[2])
time_delta = timedelta(days=num_days)

cur_date = origin_date + time_delta
print(cur_date.year, cur_date.month, cur_date.day)

"""В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
Во второй строке дано одно число days -- число дней.

Вычислите и выведите год, месяц и день даты, которая наступит, 
когда с момента исходной даты date пройдет число дней, равное days.

Примечание:
Для решения этой задачи используйте стандартный модуль datetime.
Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta 
для прибавления дней к дате.

Sample Input 1:

2016 4 20
14
Sample Output 1:

2016 5 4
Sample Input 2:

2016 2 20
9
Sample Output 2:

2016 2 29
Sample Input 3:

2015 12 31
1
Sample Output 3:

2016 1 1"""