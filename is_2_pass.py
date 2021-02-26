import requests
import re

# doc_a, doc_b = [input().strip() for _ in range(2)]
# doc_a = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'
# doc_b = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'

# Sample Input 1:
#
doc_a1 = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'
doc_b1 = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'
# Sample Output 1:
#
# Yes
# Sample Input 2:
#
doc_a2 = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'
doc_b2 = 'https://stepic.org/media/attachments/lesson/24472/sample1.html'
# Sample Output 2:
#
# No
# Sample Input 3:
#
doc_a3 = 'https://stepic.org/media/attachments/lesson/24472/sample1.html'
doc_b3 = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'
# Sample Output 3:
#
# Yes

def get_hrefs(url):
    res = requests.get(url)
    pattern = r"(https.+html)"
    return re.findall(pattern, res.text)

def is_2_pass(doc_1, doc_2):
    answ = "No"
    try:
        requests.get(doc_1)
    except:
        print(answ)
        return
    try:
        requests.get(doc_2)
    except:
        print(answ)
        return

    url_list = get_hrefs(doc_1)
    for url_n in url_list:
        url_lst1 = get_hrefs(url_n)
        if doc_2 in url_lst1:
            answ = "Yes"
            break
    print(answ)

is_2_pass(doc_a1, doc_b1)
is_2_pass(doc_a2, doc_b2)
is_2_pass(doc_a3, doc_b3)
is_2_pass('qqq', doc_b1)
is_2_pass(doc_a1, 'qqq')

"""
Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. 
внутри A есть тег <a href="B">, возможно с дополнительными параметрами внутри тега.

Из A можно перейти в B за два перехода если существует такой документ C, что из A 
в C можно перейти за один переход и из C в B можно перейти за один переход.

Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

Обратите внимание на то, что не все ссылки внутри HTML документа могут вести 
на существующие HTML документы.

Sample Input 1:

https://stepic.org/media/attachments/lesson/24472/sample0.html
https://stepic.org/media/attachments/lesson/24472/sample2.html
Sample Output 1:

Yes
Sample Input 2:

https://stepic.org/media/attachments/lesson/24472/sample0.html
https://stepic.org/media/attachments/lesson/24472/sample1.html
Sample Output 2:

No
Sample Input 3:

https://stepic.org/media/attachments/lesson/24472/sample1.html
https://stepic.org/media/attachments/lesson/24472/sample2.html
Sample Output 3:

Yes
"""