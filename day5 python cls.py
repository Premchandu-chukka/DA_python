'''
Input formatting
----------------


integer--> int(input())

num = int(input('enter a number:'))
print(type(num))

enter a number:4
<class 'int'>

-------------------------------------------------
Decimal / Float Input

b = float(input("Enter any decimal: "))
print(b + 7)

Enter any decimal: 8
15.0
---------------------------------------------------
String

s = input("enter a string: ")
print(type(s))

enter a string: prem
<class 'str'>
-----------------------------------------------------
List-->

nums = list(map(int,input(" enter some numbers:").split()))
print(nums)

 enter some numbers:1 2 3 4 5
[1, 2, 3, 4, 5]
--------------------------------------------------------------
Tuple-->

nums = tuple(map(int,input(" enter some numbers:").split()))
print(nums)

 enter some numbers:1 2 3 4 5
(1, 2, 3, 4, 5)
-------------------------------------------------------------
Set-->
nums = set(map(int,input(" enter some numbers:").split()))
print(nums)

 enter some numbers:1 2 3 4
{1, 2, 3, 4}

------------------------------------------------------------------
printing multiple values using commas in print().

name = 'prem'
batch = 6
print(' My name is',name,'and my batch is',batch)
print('hello!',name)

 My name is prem and my batch is 6
hello! prem
------------------------------------------------------------------
f string
name = 'prem'
batch = 6
print(f'my name is {name} and my batch is {batch}')

my name is prem and my batch is 6
--------------------------------------------------------------------
string formatting with %

name = 'prem'
batch = 6
print('my name is %s and iam from batch %d' %(name,batch))
my name is prem and iam from batch 6
---------------------------------------------------------------
'''
name = 'prem'
batch = 6
print('my name is %s and iam from batch %d' %(name,batch))
my name is prem and iam from batch 6
