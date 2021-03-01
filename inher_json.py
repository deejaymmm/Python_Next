import json

js_line = [{"name": "G", "parents": ["ZZZ"]},
                     {"name": "TH", "parents": ["ZZZ"]},
                     {"name": "G", "parents": ["ZY"]},
                     {"name": "G", "parents": ["F"]},
                     {"name": "A", "parents": []},
                     {"name": "B", "parents": ["A"]},
                     {"name": "C", "parents": ["A"]},
                     {"name": "D", "parents": ["B", "C"]},
                     {"name": "E", "parents": ["D"]},
                     {"name": "F", "parents": ["D"]},
                     {"name": "X", "parents": []},
                     {"name": "Y", "parents": ["X", "A"]},
                     {"name": "Z", "parents": ["X"]},
                     {"name": "V", "parents": ["Z", "Y"]},
                     {"name": "W", "parents": ["V"]}]

# js_line = json.loads(input())

inher_dict = {}
for line in js_line:
    if line['name'] not in inher_dict:
        inher_dict[line['name']] = [line['name']]
    for cur_parent in line['parents']:
        if cur_parent not in inher_dict:
            inher_dict[cur_parent] = [cur_parent]
for line in js_line:
    for cur_parent in line['parents']:
        inher_dict[cur_parent] += [line['name']]
# print(inher_dict)

def is_parent(parent, child):
    if child not in inher_dict:
        return False
    if parent in inher_dict[child] or parent == child:
        # !!! "Гарантируется, что класс не наследуется сам от себя
        # (прямо или косвенно)"
        return True
    else:
        flag = False
        for cur_parent in inher_dict[child]:
            if cur_parent != child:
                flag = is_parent(parent, cur_parent)
            if flag:
                break
    return flag


parents = {}
for cur_child in inher_dict:
    for cur_parent in inher_dict[cur_child]:
        # print(cur_parent, cur_child)
        if cur_parent not in parents:
            parents[cur_parent] = 0
# print(parents)

for cur_parent_out in parents:
    for cur_child in inher_dict:
        for cur_parent_in in cur_child:
            if is_parent(cur_child, cur_parent_out):
                parents[cur_parent_out] += 1
                break

for cur_parent in sorted(parents):
    print(cur_parent + ' : ' + str(parents[cur_parent]))

"""
Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют 
классам. У каждого JSON-объекта есть поле name, которое содержит имя класса, 
и поле parents, которое содержит список имен прямых предков.

Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, 
{"name": "C", "parents": ["A"]}]

Эквивалент на Python:

class A:
    pass

class B(A, C):
    pass

class C(A):
    pass

Гарантируется, что никакой класс не наследуется от себя явно или косвенно, 
и что никакой класс не наследуется явно от одного класса более одного раза.

Для каждого класса вычислите предком скольких классов он является и выведите 
эту информацию в следующем формате.

<имя класса> : <количество потомков>

Выводить классы следует в лексикографическом порядке.

Sample Input:

[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, 
{"name": "C", "parents": ["A"]}]
Sample Output:

A : 3
B : 1
C : 2
"""