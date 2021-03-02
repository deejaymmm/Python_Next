import requests

with open("input2.txt") as read_file, open("output2.txt", "w") as write_file:
    lines = [line.strip() for line in read_file]
    for line in lines:
        api_url = f"http://numbersapi.com/{line}/math"
        params = {'json': 'true'}
        res = requests.get(api_url, params=params)
        data = res.json()
        print(data['text'])
        if data['found']:
            write_file.writelines("Interesting\n")
        else:
            write_file.writelines("Boring\n")

"""
В этой задаче вам необходимо воспользоваться API сайта numbersapi.com

Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли 
интересный математический факт об этом числе.

Для каждого числа выведите Interesting, если для числа существует интересный 
факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют 
числа во входном файле.

Пример запроса к интересному числу:
http://numbersapi.com/31/math?json=true

Пример запроса к скучному числу:
http://numbersapi.com/999/math?json=true

Пример входного файла:
31
999
1024
502

Пример выходного файла:
Interesting
Boring
Interesting
Boring
"""

