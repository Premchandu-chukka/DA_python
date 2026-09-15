'''

lambda function
--------------
--> lambda function is small anonymous function
--> lambda can take n number arguments, but only with one expression
--> the function is defined by using lambda keyword

syntax-->lambda arguments : expression

add_ = lambda a,b,c:a+b+c
print(add_(15,9,22))

output:
46
----------------------------------------------
even = lambda num : num%2==0
print(even(10))

output:
True
----------------------------------------------

greater = lambda a,b: a if a>b else b
print(greater(10,20))

output:
20
---------------------------------------------
cube = lambda a: a**3
print(cube(5))

output:
125
---------------------------------------------

filter()
----------
--> filter() function will perform only on selected elements of iterables
syntax: filter(lambda arguments: expression, iterable)

nums = [1,3,2,4,6,5,7]
data_ = filter(lambda a: a%2==0,nums)
print(tuple(data_))

output:
(2, 4, 6)
-----------------------------------------------------------------------------

map()
--> map()function will perform on every elements of iterables
syntax: map(lambda arguments: expression, iterable)

nums = [1,3,2,4,6,5,7]
data_ = map(lambda a: a*2,nums)
print(list(data_))

output:
[2, 6, 4, 8, 12, 10, 14]
----------------------------------------------------------------------

reduce()
--> The reduce() function repeatedly applies a function to the elements and reduces them to one final value.
--> It is available in the functools module.
Syntax: reduce(lambda arguments: expression, iterable)
from functools import reduce
nums = [1,3,2,4,6,5,7]
data_ = reduce(lambda a,b: a*b,nums)
print(data_)

output:
5040
'''
from functools import reduce
nums = [1,3,2,4,6,5,7]
data_ = reduce(lambda a,b: a*b,nums)
print(data_)
