from xml.etree import ElementTree


def foo(cur_elem):
    global level
    level += 1
    for element in cur_elem:
        color_dict[element.attrib['color']] += level
        foo(element)
        level -= 1


inp_line = input().strip()
# inp_line = '<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>'
# inp_line = '<cube color="blue"><cube color="red"><cube color="green"><cube color="blue"><cube color="red"><cube color="red"></cube></cube></cube></cube></cube><cube color="blue"><cube color="green"></cube></cube><cube color="blue"></cube></cube>'
root = ElementTree.fromstring(inp_line)
color_dict = {'red': 0, 'green': 0, 'blue': 0}
level = 1
color_dict[root.attrib['color']] += level
foo(root)
print(str(color_dict['red']) + ' ' +
      str(color_dict['green']) + ' ' +
      str(color_dict['blue']))
"""
Вам дано описание пирамиды из кубиков в формате XML.
Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue).
Для каждого кубика известны его цвет, и известны кубики, расположенные прямо 
под ним.

Пример:

<cube color="blue">
  <cube color="red">
    <cube color="green">
    </cube>
  </cube>
  <cube color="red">
  </cube>
</cube>
 
Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий 
корню XML документа имеет ценность 1. Кубики, расположенные прямо под ним, 
имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками, 
имеют ценность 3. И т. д.

Ценность цвета равна сумме ценностей всех кубиков этого цвета.

Выведите через пробел три числа: ценности красного, зеленого и синего цветов.
Sample Input:

<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>
Sample Output:

4 3 1
"""