'''
Functions
-----------
--> A function is a block of code that can be executed only when it is called...
--> If the function starts with the def keyword then the line is called as the definition line, where we can define a function name
--> And if we want to execute the program in the function, need to call with function name define at def line.
syntax:
------

def function_name(parameters):
    pass
function_name(arguments)

eg:

def add_(a,b):
    print(a+b)
add_(5,7)

output:
12
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Arguments
----------

positional arguments
--------------------
--> The arguments should be same at def line and calling, incase if they are not same number it will raise an error
num = 0
num_2 = 1
def feb_(num,num_2):

    print(num,num_2,end=" ")

    for i in range(1,10):
        num_3 = num + num_2
        num =num_2
        num_2 = num_3
        print(num_3,end=" ")
feb_ (num,num_2)

output:
0 1 1 2 3 5 8 13 21 34 55
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

default arguments
-----------------
--> The default arguments where the function will only considered the data at calling, even though data present at def line 


def feb_(num,num_2):
    print(num+num_2)
feb_([1,3],[3,6])

output:
[1, 3, 3, 6]

def prime(i, count=0):
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1

    if count == 2:
        print(f"{i} is a prime number")
    else:
        print(f"{i} is not a prime number")


num = int(input("Enter a number: "))
prime(num)

output:
Enter a number: 15
15 is not a prime number
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Keyword arguments
-----------------
--> keyword arguments are sending arguments in pair(a=2),and the pass order is not considered here


def data(age,name,batch,location):
    print(name)
    print(age)
    print(batch)
    print(location)
data(name="prem",age="25",location="vsp",batch=6)

output:
prem
25
6
vsp
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Variable length argument
------------------------
-->Adding a(* call it as args) before a variable at parameter we can pass tuple of arguments and can be access with indexing

def all(*name):
    print(name[1])
all("prem","chand","chukka")

output:
chand
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Keyword arguments
-----------------
-->When we use ** before a parameter in a function, Python collects multiple keyword arguments into a dictionary.

def details(**data):
    print(data)
details(name="prem",age="25",location="vsp",batch=6)

output:
{'name': 'prem', 'age': '25', 'location': 'vsp', 'batch': 6}
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Return
------
--> return keyword is used inside the function, once the return is executed means it will get back to calling function with certain return values

eg:
def all_(a,b):
    return a-b
print(all_(7,9))

output:
-2
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''


def all_(a,b):
    return a-b
print(all_(7,9))


