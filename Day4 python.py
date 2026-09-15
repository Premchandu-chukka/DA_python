Concatination
--------------
-->The + will behave in two ways for numeric it works normally(i.e it adds values)..
but for other data types like str, list, tuple it concatenated.


operators
-----------

--> The operators are used to perform operations in variables and the values..

1. Arthematic operator
-------------------------------------------------------------------------
+, -, *, /, //, %


----------------------
+--> to add the values
eg:
num = 3
num_2 = 6
print(num + num_2)
--------------------

- -->To subtract the values
eg:
num = 9
num_2 = 6
print(num - num_2)
-------------------------

*--> multiplies values
num = 3
num_2 = 6
print(num * num_2)
------------------------
/--> quotient will be displayed with decimal points

num = 9
num_2 = 3
print(num / num_2)
output:3.0
----------------------

//--> quotient will be displayed without decimal points
num = 9
num_2 = 3
print(num // num_2)
 output:3
--------------------

%--> displayes remainder after divison
num = 9
num_2 = 3
print(num % num_2)
output:0(remainder)
----------------------------------------------------------------

2. Assignment operator
-----------------------
=, +=, -=, *=, /=, %=

+= --> It is increment operator
a = 0 
print(a)
a += 1
print(a)

-= --> Decrement operator
b = 15
b -= 5
print(b)

*=-->
b = 15
b *= 5
print(b)

/=-->

s = 15
s /= 5
print(s)

%=-->

s = 15
s %= 5
print(s)
------------------------------------------------------------------------

3. Comparison operator

==, >=, <=, !=, <, >

==
num = 15
num_2 = 9
print(num == num_2)
 output: false

!=
num = 15
num_2 = 9
print(num != num_2)
 output: true

>
num = 15
num_2 = 9
print(num > num_2)
 output: true

<
num = 15
num_2 = 9
print(num < num_2)
 output: false

>=
num = 15
num_2 = 9
print(num >= num_2)
 output: true

<=
num = 15
num_2 = 9
print(num <= num_2)
 output: false
--------------------------------------------------------------------------------
4. Logical operator
------------------------------
and-->

num = 15
num_2 = 9
print (num >= num_2 and num <=10)

or-->
num = 15
num_2 = 9
print (num >= num_2 and num <=10)

not-->
num = 1
num_2 = 9

print(not(num >= num_2 or num <=10))
------------------------------------------------------------------------------------
5. Identity operator
is
a = [1,2]
b = [1,2]
print(a == b)
print(a is b)
output: true
        false

is not--> location will change
a = [1,2]
b = [1,2]
print(id(a))
print(id(b))
123456789
123456987
------------------------------------------------------------------------------------


6. Membership operator
whether the given term is available in or not

nums = 'python is programming language'
print('y' in nums)
print('i'not in nums)

output:
true
false
------------------------------------------------------------------------------------
7. Bitwise operator

&--> bitwise and

a = 5
b = 3

print(a & b)

5 = 0101
3 = 0011
---------
& = 0001
---------------------------------------------
|--> bitwise or
a = 9
b = 6

print(a | b)

9 = 1001
6 = 0110
---------
| = 1111

-------------------------------------------------
^--> bitwise XOR

a = 12
b = 10

print(a ^ b)

12 = 1100
10 = 1010
---------
 ^ = 0110
----------------------------------------------------
>>--> Right shift

a = 8

print(a >> 1)

8 = 1000

1000 >> 1
      ↓
0100
0100 = 4
------------------------------------------------------
<<--> left shift
a = 3

print(a << 1)

3 = 0011

0011 << 1
     ↓
0110
0110 = 6
-------------------------------------------------------