'''
Scope of variables
------------------
1.Local variables
------------------
--> A variable is defined inside the function we call it as a local variable, where the variable can only acess with in that function

eg:

def display():
    name = 'prem'
    print(name)
display()

output:
prem



2.Global variables
--> A variable that is defined outside the function call and it can be acess anywhere through out program

num = 15
def display():
    print(num)
display()
print(num)

output:
15
15
------------------
num = 15
print(num)
def display():
    global num
    num = 9
display()
print(num)

output:
15
9

global keyword
---------------
--> global is a keyword used to reassign new values to a variable that were already defined outside the function call

-----------------------------------------------------------------------------------------------
Passing by value
---------------


def even_odd(num):
    if num % 2 == 0:
        print(f"{num}is even")
    else:
        print(f"{num}is odd")
even_odd(159)

output:
159is odd
-------------------
passing by variable
-------------------

num = 10
def even_odd(num):
    if num % 2 == 0:
        print(f"{num}is even")
    else:
        print(f"{num}is odd")
even_odd(num)

output:
10is even
-----------------------------------------------------------------------------------------------

Recursive function
------------------
--> The function call itself until the base condition met...

def fac(a):
    if a==0 or a==1:
        return a
    return a*fac(a-1)
print(fac(4))

output:
24
'''

def fac(a):
##    if a==0 or a==2:
      #  return a
    return a*fac(a-1)
print(fac(5))
