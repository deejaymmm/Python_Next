def s(a, *vs, b=10):
   res = a + b
   for v in vs:
       res += v
   return res
print(s())

"""Дана функция s:

def s(a, *vs, b=10):
   res = a + b
   for v in vs:
       res += v
   return res
В результате каких вызовов данная функция вернет число 31?

False   s(11, 10, 10)
True    s(11, b=20)
True    s(11, 10)
True    s(5, 5, 5, 5, 1)
False   s(b=31)
False   s(0, 0, 31)
False   s(b=31, 0)
True    s(21)
True    s(11, 10, b=10)
"""