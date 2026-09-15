'''
Tokens
------
-->Tokens are the small unit in the python..

1. Identifier: It is a name of variable or function or class
-----------
variable-->

num = 'Python'
print(type(num))
-----------

functions-->

def add_(a,b):
print(a+b)

add_(4,5)
------------

class-->

class details:
  pass
per_1 = details
----------------------------------------------------------------------------

2.Keywords: These are already saved in python for a specific reason to run..
----------

eg-->

if
else
for
while
return
print
----------------------------------------------------------------------------

3.Literals: these are the data types that need to be stored in variables...

eg-->
num = 9
name = 'prem'
------------------------------------------------------------------------------

4.Operator +, -, *, /, =
------------------------------------------------------------------------------

5.Statements: These are the instructions given to the program..

num = 15

let us consider 
age = 20
if age >= 15:
       print(age)
----------------------------------------------------------------------------

comments:

once the commands are open the lines will never execute in python file

1. single line comment(#) 
           |
 This is used to comment only one line
example:
          age = 20
if age >= 15:    #this check whether the age is greater or equal
print(age)

2. multi line comment('''  ''', """  """)
              |
 Used to comment more than one file
---------------------------------------------------------------------------


variables rules
-------------
Bad ways
----------
--> can't use number at 1st place
--> can't use special character anywhere
--> can't use space
--> keywords
eg:
2num = 15
$num = 09
n num = 04
if = 07
-------------
Good ways
-----------
--> we can use both uppercase and lowercase letters
--> (_)underscore can be used
eg:
nUm = 99
NUM = 10
num_4 = 28

a = {'name' : 'prem',
     'AC_num' : '123456789'}
b = {'name' : 'pchand',
     'AC_num' : '1258741963'}

sbi_chand_details = {'name' : 'prem',
                     'AC_num' : '987654321'}


num_3, num_4 =56,65
print(num_3)
print(num_4)

  Swapping of two variables

a , b = 45,54
print('a=',a)
print('b=',b)
a, b = b, a
print('a=',a)
print('b=',b)
---------------
'''