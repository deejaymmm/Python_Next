import requests
import re

# doc = input().strip()
doc = 'http://pastebin.com/raw/7543p0ns'

res = requests.get(doc)
lines = res.text.splitlines()
site_list = []
for line in lines:
    pattern = r'(?:<a\s.*?)(?:href=[\'|\"]?.*?)(?:[\w+?|\-]://?)(\w[\w+?|\.|\-]+)'
        # не "жадное" вхождение (первое, а не все)
    try:
        cur_site = (re.findall(pattern, line.strip())[0])
    except:
        cur_site = ''
    if cur_site != '' and cur_site not in site_list:
        site_list.append(cur_site)
site_list.sort()
for cur_site in site_list:
    print(cur_site)

"""
Вашей программе на вход подается ссылка на HTML файл.
Вам необходимо скачать этот файл, затем найти в нем все ссылки вида 
<a ... href="..." ... > и вывести список сайтов, на которые есть ссылка.

Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. 
То есть, это последовательность символов, которая следует сразу после 
символов протокола, если он есть, до символов порта или пути, если они есть, 
за исключением случаев с относительными ссылками вида
<a href="../some_path/index.html">.

Сайты следует выводить в алфавитном порядке.

Пример HTML файла:

<a href="http://stepic.org/courses">
<a href='https://stepic.org'>
<a href='http://neerc.ifmo.ru:1345'>
<a href="ftp://mail.ru/distib" >
<a href="ya.ru">
<a href="www.ya.ru">
<a href="../skip_relative_links">

Пример ответа:

mail.ru
neerc.ifmo.ru
stepic.org
www.ya.ru
ya.ru
"""