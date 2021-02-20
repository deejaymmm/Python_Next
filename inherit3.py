inp_lines = [  # список введённых строк
    'G : F',  # сначала отнаследуем от F, потом его объявим, корректный алгоритм все равно правильно обойдёт граф, независимо что было раньше: наследование или объявление
    'A',
    'B : A',
    'C : A',
    'D : B C',
    'E : D',
    'F : D',
    # а теперь другая ветка наследования
    'X',
    'Y : X A',  # свяжем две ветки наследования для проверки, обошла ли рекурсия предков Z и предков Y в поисках A
    'Z : X',
    'V : Z Y',
    'W : V'
]

# inp_lines = [input() for i in range(int(input()))]
# inp_lines = ['A', 'B : A', 'C : A', 'D : B C']
# print(inp_lines)
inher_dict = {}
for line in inp_lines:
    cur_str = line.split()
    if line[0] not in inher_dict:
        cur_lst = [line[0]]
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

inp_lines = [  # список введённых запросов
    'A G',      # Yes   # A предок G через B/C, D, F
    'A Z',      # No    # Y потомок A, но не Y
    'A W',      # Yes   # A предок W через Y, V
    'X W',      # Yes   # X предок W через Y, V
    'X QWE',    # No    # нет такого класса QWE
    'A X',      # No    # классы есть, но они нет родства :)
    'X X',      # Yes   # родитель он же потомок
    '1 1',      # No    # несуществующий класс
]

# inp_lines = [input() for i in range(int(input()))]
# inp_lines = ['A B', 'B D', 'C D', 'D A']
# print(inp_lines)
for cur_req in inp_lines:
  cur_req_lst = cur_req.split()
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
No"""