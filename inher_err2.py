# inp_lines = [input() for i in range(int(input()))]
# inp_lines = ['ArithmeticError', 'ZeroDivisionError : ArithmeticError', 'OSError', 'FileNotFoundError : OSError']
inp_lines = [
    'a',
    'b : a',
    'c : a',
    'f : a',
    'd : c b',
    'g : d f',
    'i : g',
    'm : i',
    'n : i',
    'z : i',
    'e : m n',
    'y : z',
    'x : z',
    'w : e y x'
    ]
# print(inp_lines)
inher_dict = {}
for line in inp_lines:
    cur_str = line.split()
    if cur_str[0] not in inher_dict:
        cur_lst = [cur_str[0]]
        inher_dict[cur_str[0]] = cur_lst
    if len(cur_str) > 2:
        for i in range(2, len(cur_str)):
            if cur_str[i] not in inher_dict[cur_str[0]]:
                cur_lst = inher_dict[cur_str[0]]
                cur_lst.append(cur_str[i])
                inher_dict[cur_str[0]] = cur_lst
# print(inher_dict)

def is_parent(parent, child):
    if child not in inher_dict:
        return False
    if parent in inher_dict[child] or parent == child: # !!! "Гарантируется, что класс не наследуется сам от себя (прямо или косвенно)"
        return True
    else:
        flag = False
        for cur_parent in inher_dict[child]:
            if cur_parent != child:
                flag = is_parent(parent, cur_parent)
            if flag:
                break
    return flag

# inp_lines = [input() for i in range(int(input()))]
# inp_lines = ['ZeroDivisionError', 'OSError', 'ArithmeticError', 'FileNotFoundError']
inp_lines = [
    'y',
    'm',
    'n',
    'm',
    'd',
    'e',
    'g',
    'a',
    'f',
    ]
# print(inp_lines)
before_lst = []
child_lst = []
for cur_req in inp_lines:
    for cur_bef in before_lst:
        if is_parent(cur_bef, cur_req) and cur_req not in child_lst:
            child_lst.append(cur_req)
    before_lst.append(cur_req)
for item in child_lst:
    print(item)

"""
Вам дано описание наследования классов исключений в следующем формате.
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
так как ранее в коде будет пойман их предок. Но Антон не помнит какие исключения наследуются от каких. 
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
"""