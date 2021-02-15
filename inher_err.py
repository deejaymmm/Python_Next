num_str = int(input())
inher_dict = {}
for cur_num_str in range(num_str):
  cur_str = input().strip().split()
  if cur_str[0] not in inher_dict:
    cur_lst = []
    cur_lst.append(cur_str[0])
    inher_dict[cur_str[0]] = cur_lst
  if len(cur_str) > 2:
    for num_parent in range(2, len(cur_str)):
      if cur_str[num_parent] not in inher_dict[cur_str[0]]:
        cur_lst = inher_dict[cur_str[0]]
        cur_lst.append(cur_str[num_parent])
        inher_dict[cur_str[0]] = cur_lst

def is_child(child, parent):
    if child not in inher_dict:
        return False
    if child == parent:
        return False
    if parent in inher_dict[child]:
        return True
    flag = False
    for cur_par in inher_dict[child]:
        if cur_par != child:
            flag = is_child(child, cur_par)
    return flag

before_lst = []
child_set = set()
num_req = int(input())
for cur_num in range(0, num_req):
    cur_req = input().strip()
    for cur_bef in before_lst:
        if is_child(cur_req, cur_bef):
            child_set.add(cur_req)
    before_lst.append(cur_req)

for item in child_set:
    print(item)

"""Вам дано описание наследования классов исключений в следующем формате.
<имя исключения 1> : <имя исключения 2> <имя исключения 3> ... <имя исключения k>
Это означает, что исключение 1 наследуется от исключения 2, исключения 3, и т. д.

Или эквивалентно записи:
class Error1(Error2, Error3 ... ErrorK):
    pass

Антон написал код, который выглядит следующим образом.

try:
   foo()
except <имя 1>:
   print("<имя 1>")
except <имя 2>:
   print("<имя 2>")
...
Костя посмотрел на этот код и указал Антону на то, что некоторые исключения можно не ловить, 
так как ранее в коде будет пойман их предок. 
Но Антон не помнит какие исключения наследуются от каких. 
Помогите ему выйти из неловкого положения и напишите программу, 
которая будет определять обработку каких исключений можно удалить из кода.

Важное примечание:
В отличие от предыдущей задачи, типы исключений не созданы.
Создавать классы исключений также не требуется
Мы просим вас промоделировать этот процесс, и понять какие из исключений можно и не ловить, 
потому что мы уже ранее где-то поймали их предка.

Формат входных данных
В первой строке входных данных содержится целое число n - число классов исключений.

В следующих n строках содержится описание наследования классов. 
В i-й строке указано от каких классов наследуется i-й класс. 
Обратите внимание, что класс может ни от кого не наследоваться. 
Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), 
что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число m - количество обрабатываемых исключений.
Следующие m строк содержат имена исключений в том порядке, в каком они были написаны у Антона в коде.
Гарантируется, что никакое исключение не обрабатывается дважды.

Формат выходных данных
Выведите в отдельной строке имя каждого исключения, обработку которого можно удалить из кода, 
не изменив при этом поведение программы. Имена следует выводить в том же порядке, 
в котором они идут во входных данных.

Пример теста 1
Рассмотрим код

try:
   foo()
except ZeroDivision :
   print("ZeroDivision")
except OSError:
   print("OSError")
except ArithmeticError:
   print("ArithmeticError")
except FileNotFoundError:
   print("FileNotFoundError")


...


По условию этого теста, Костя посмотрел на этот код, и сказал Антону, 
что исключение FileNotFoundError можно не ловить, ведь мы уже ловим OSError -- предок FileNotFoundError
Sample Input:

4
ArithmeticError
ZeroDivisionError : ArithmeticError
OSError
FileNotFoundError : OSError
4
ZeroDivisionError
OSError
ArithmeticError
FileNotFoundError
Sample Output:

FileNotFoundError


[+] Test #1. OK
[ ] Test #2. Wrong answer
[ ] Test #3. Wrong answer
[ ] Test #4. Wrong answer
[+] Test #5. OK
[ ] Test #6. Wrong answer
[ ] Test #7. Wrong answer
[ ] Test #8. Wrong answer
[ ] Test #9. Wrong answer
[ ] Test #10. Wrong answer
[ ] Test #11. Wrong answer
[ ] Test #12. Wrong answer
[+] Test #13. OK
[ ] Test #14. Wrong answer
[ ] Test #15. Wrong answer
[ ] Test #16. Wrong answer

3 of 16 test(s) passed."""
