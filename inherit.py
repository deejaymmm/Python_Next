num_str = int(input())
inher_dict = {}
for cur_num_str in range(num_str):
  cur_str = input().split()
  if cur_str[0] not in inher_dict:
    cur_lst = []
    cur_lst.append(cur_str[0])
    inher_dict[cur_str[0]] = cur_lst
  if len(cur_str) > 2:
    for i in range(2, len(cur_str)):
      if cur_str[i] not in inher_dict[cur_str[0]]:
        cur_lst = inher_dict[cur_str[0]]
        cur_lst.append(cur_str[i])
        inher_dict[cur_str[0]] = cur_lst

def is_parent(parent, child):
    if parent in inher_dict[child]:
      return True
    else:
      for cur_parent in inher_dict[child]:
        if cur_parent != child and cur_parent in inher_dict:
          return is_parent(parent, cur_parent)
    return False

num_req = int(input())
for cur_req in range(num_req):
  cur_req_lst = input().split()
  if is_parent(cur_req_lst[0], cur_req_lst[1]):
    print('Yes')
  else:
    print('No')

"""Вам дано описание наследования классов в следующем формате.
<имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.

Или эквивалентно записи:

class Class1(Class2, Class3 ... ClassK):
    pass
Класс A является прямым предком класса B, если B отнаследован от A:


class B(A):
    pass


Класс A является предком класса B, если
A = B;
A - прямой предок B
существует такой класс C, что C - прямой предок B и A - предок C

Например:
class B(A):
    pass

class C(B):
    pass

# A -- предок С


Вам необходимо отвечать на запросы, является ли один класс предком другого класса

Важное примечание:
Создавать классы не требуется.
Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.
Формат входных данных
В первой строке входных данных содержится целое число n - число классов.

В следующих n строках содержится описание наследования классов. 
В i-й строке указано от каких классов наследуется i-й класс. 
Обратите внимание, что класс может ни от кого не наследоваться. 
Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), 
что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число q - количество запросов.

В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.

Формат выходных данных
Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, 
и "No", если не является.

Sample Input:

4
A
B : A
C : A
D : B C
4
A B
B D
C D
D A
Sample Output:

Yes
Yes
Yes
No
Напишите программу. Тестируется через stdin → stdout
Верно решили 13 973 учащихся
Из всех попыток 16% верных
 Пока неправильно, попробуйте еще раз!
[+] Test #1. OK
[ ] Test #2. Wrong answer
[+] Test #3. OK
[+] Test #4. OK
[ ] Test #5. Wrong answer
[+] Test #6. OK
[+] Test #7. OK
[+] Test #8. OK
[+] Test #9. OK
[+] Test #10. OK
[+] Test #11. OK
[+] Test #12. OK
[+] Test #13. OK
[+] Test #14. OK
[+] Test #15. OK
[+] Test #16. OK

14 of 16 test(s) passed."""