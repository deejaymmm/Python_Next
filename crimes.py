import csv
import re

crime_dict = {}
with open("Crimes.csv") as f:
    reader = csv.reader(f)
    headers = next(reader)
    for row in reader:
        cur_year = re.findall(r'(?:\d\d/\d\d/)(\d{4})', row[2].strip())
        if cur_year[0] == '2015':
            crime = row[5]
            if crime not in crime_dict:
                crime_dict[crime] = 1
            else:
                crime_dict[crime] += 1

crime_max = ''
num_max = 0
for crime in crime_dict:
    cur_num = crime_dict[crime]
    if cur_num > num_max:
        crime_max = crime
        num_max = cur_num

print(crime_max, num_max)

"""
Вам дана частичная выборка из датасета зафиксированных преступлений, 
совершенных в городе Чикаго с 2001 года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано 
максимальное число раз в 2015 году.

Файл с данными:
Crimes.csv
"""
