l = list(range(1,101))

l

help(filter)

filter(lambda f: True if(f%2 == 0) else False, l)

lEven = filter(lambda f: True if(f%2 == 0) else False, l)

lEven

for i in lEven: print(i)

lEven = filter(lambda f:  True if (f%2== 0) else False,l)
lEven = filter(lambda f: f%2 == 0, l)

for i in lEven: print(i)

lEven = filter(lambda f: f%2==0, l)

lSqr = map(lambda f: f*f,lEven)

import functools as ft

help(ft.reduce)

lSqr.reduce(lambda x,y: x+y, lSqr)

