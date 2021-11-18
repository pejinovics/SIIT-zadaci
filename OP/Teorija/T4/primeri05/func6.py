>>> class A(object): pass
...
>>> a = A()
>>> a.value = 1
>>> def set_a(val):
...   a.value = val
...
>>> a.value
1
>>> set_a(5)
>>> a.value
5