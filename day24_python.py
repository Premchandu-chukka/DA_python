'''
File Handling and Exception Handling
-----------------------------------
-->This is the way handling errors
--> we can write n number of exceptions for one code written at try block

try:
======
--> the try block, where we can write code which may contain error
syntax-->
try:
    codelines
    
------------------------------------------------------------------------
except
======
--> this will handle error that are raised at try block
syntax-->
except ErrorName:
    print('Error Name')
try:
    print(6/0)
    print(num)
except ZeroDivisionError:
    print('Not Divisible by Zero') 
except NameError:
    print('Name Error')


------------------------------------------------------------------------
else
=====
--> the else block will only execute, if try block has no error 

try:
    print('Hello')
except ZeroDivisionError:
    print('Not Divisible by Zero')
except NameError:
    print('Name Error')
else:
    print('No Error')
--------------------------------------------------------------------------
finally
=======
--> the finally block will be executed even there are errors present in try block

try:
    print('5/0')
except ZeroDivisionError:
    print('Not Divisible by Zero')
except NameError:
    print('Name Error')
else:
    print('No Error')
finally:
    print('Hello')
==========================================================================================
File Handling
=============
--> The file handler is a object, which is used to create, update, read, and delete...


modes
-----
r --> the (r) mode is used when the read() function is used

w

a

x

functions
----------
read()
write()
append()
'''

with open ('hey.txt','x') as file:
   file.write(" my friend")
