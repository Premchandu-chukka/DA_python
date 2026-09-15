'''
loops:
------
for statement
-------------
-->for loop is used to iterate over a squence or iterable datatypes
--> here in the below statements j is used to define this variable at run to store values from iterable datatype

nums = [13,4,15,78]
for j in nums:
    print(j)

output: 13
         4
        15
        78
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------   


else in for
----------
--> unlike if-else, else block in for statement is executed after completed of all iterations

nums = [13,4,15,78]
for j in nums:
    print(j)
else:
    print('for loop ended')

output:
13
4
15
78
for loop ended
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------   

break
-------
--> break is used to stop iteration on the condion given

nums = [1,2,3,4,5,6,7,8,9]
for j in nums:
    print(j)
    if j ==3:
         break
  
    
output:
1
2
3
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------   

continue
--------
-->the continue is keyword used to skip the current iteration based on the condition given

nums = [1,2,3,4,5,6,7,8,9]
for j in nums:
   
    if j ==3:
         continue
    print(j)

    
output:
1
2
4
5
6
7
8
9
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------   

pass
-----
-->A pass is called as a space holder, that is used after statements like(if, for, else) not to raise any error


for j in range(1,12):
    if j == 9:
     pass
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------   

assert
------
-->assert is a keyword used to check the condition, incase the condion is false it will raise the error(Assertion Error)

 age = 15
assert age>=18, "not eligible to vote"
print("eligible to vote")

output:
    assert age>=18, "not eligible to vote"
AssertionError: not eligible to vote


eg:
age = 19
assert age>=18, "not eligible to vote"
print("eligible to vote")

output:
eligible to vote
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------   

while
------

num =1
while num<5:
    print(num)
    num +=1

output:
1
2
3
4


task: approaches

find the number is even or odd
remove duplicates from list
armstrong number
no of vowels in the string
count no of words in the string
'''
num =1
while num<5:
    print(num)
    num +=1






