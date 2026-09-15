'''
Tuple
-----
--> Tuple is a collection of different datatypes that are seprated by , and represented by ()
--> It is immutable
--> we can pass a tuple values and that can be assign to the variables, but should match same number variables and values inside the tuple...
eg :
--
t = (1,'python',[3,4],(7,9))

indexing

eg
--

t = (1,'python',[3,4],(7,9))
print(t[1][1])

index()
--------

--> if the item is not present in the tuple, it will raise valueError

eg
--

t = (1,'Python',[3,4],(7,9))
print(t.index('python'))

len()
--------

eg :

t = (1,'Python',[3,4],(7,9))
print(len(t))

    eg: name , age , num = ('teja' , 23 , 9052925035)
        print(name)
        print(age)
        print(num)

max()
-----
--> used to find out the max value from the tuple

eg
---
so = (67,8,75,33)
print(max(so))

o/p : 75

min()
-----
--> used to find out the min value from the tuple

eg
---

so = (67,8,75,33,8,34,8)
print(min(so))

o/p : 8

count()
--------
--> used to count an item present in the tuple
eg
---

so = (67,8,75,33,8,34,8)
print(min(so))

'''

so = list('python')
print(so)
