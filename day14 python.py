'''
Even number
----------
ran_ = int(input("enter a number:"))
for j in range(1,ran_+1):
    if j % 2 == 0:
         print(f"{j}even number")
    else:
         print(f"{j}odd number")


output:
enter a number:10
1odd number
2even number
3odd number
4even number
5odd number
6even number
7odd number
8even number
9odd number
10even number
---------------------------------------------------------------------------------------------------
odd number
----------
ran_ = int(input("enter a number:"))
for j in range(1,ran_+1):
    if j % 2 != 0:
        print(f"{j}odd number")

output:
enter a number:10
1odd number
3odd number
5odd number
7odd number
9odd number
---------------------------------------------------------------------------------------------------
even numbers in a list
----------------------
nums = [23,52,24,36,78]
for j in nums:
    if j % 2 == 0:
        print(f"{j}even number")

output:
52even number
24even number
36even number
78even number
---------------------------------------------------------------------------------------------------
even numbers in a list
----------------------
nums = [23,52,24,36,78]
for j in nums:
    if j % 2 != 0:
        print(f"{j}odd number")


output:
23odd number
27odd number
7odd number

---------------------------------------------------------------------------------------------------
given number is even or odd
---------------------------

j= int(input("enter a number:"))
if j % 2 == 0:
    print(f"{j}even number")
else:
    print(f"{j} odd number")

output:
enter a number:25
25 odd number
enter a number:14
14even number
---------------------------------------------------------------------------------------------------
vowels in words
--------------
words = input("enter a word:")
vowels='aeiouAEIOU'
count = 0
for i in words:
    if i in vowels:
        count+=1
        print(f"{i} is not vowel")
print(count)

output:
enter a word:python is programming language
o is not vowel
i is not vowel
o is not vowel
a is not vowel
i is not vowel
a is not vowel
u is not vowel
a is not vowel
e is not vowel
---------------------------------------------------------------------------------------------------
not vowels in words
--------------------

words = input("enter a word:")
vowels='aeiouAEIOU '
count = 0
for i in words:
    if i not in vowels:
        count+=1
        print(f"{i} is not vowel")

output:
enter a word:python is programming language
p is not vowel
y is not vowel
t is not vowel
h is not vowel
n is not vowel
s is not vowel
p is not vowel
r is not vowel
g is not vowel
r is not vowel
m is not vowel
m is not vowel
n is not vowel
g is not vowel
l is not vowel
n is not vowel
g is not vowel
g is not vowel
---------------------------------------------------------------------------------------------------

removing duplicate values from list and copying in new list
-----------------------------------------------------------
digits=[1,6,2,4,2,3,6]
empty = []
for i in digits:
    if i not in empty:
        empty.append(i)
print(empty)

output:
[1, 6, 2, 4, 3]

count no.of words in list
-------------------------
words = 'python is a programming language'
cou = words.split(' ')
print(cou)
print(len(cou))

output:
['python', 'is', 'a', 'programming', 'language']
5

---------------------------------------------------------------------------------------------------
'''
##digits=(1,6,2,4,2,3,6)
##empty = []
##for i in digits:
##    if i not in empty:
##        empty.append(i)
##print(tuple(empty))

words = 'python is a programming language'
cou = words.split(' ')
#print(cou)
print(len(cou))

     
