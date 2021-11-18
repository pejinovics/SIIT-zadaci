>>> a = 0
>>> def get_a():
...   return a
...
>>> def set_a(val):
...   a = val
...
>>> get_a()
0
>>> a = 3
>>> get_a()
3
>>> set_a(4)
>>> a
3
