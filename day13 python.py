'''
prime number
------------

limit_ = 10

for i in range(1, limit_ + 1):
    count = 0

    for j in range(1, i + 1):
        if i % j == 0:
            count += 1

    if count == 2:
        print(f"{i} is a prime number")
    else:
        print(f"{i} is not a prime number")
    print(i)
--------------------------------------------------------------------------------------------       

pattern printing using *
------------------------------------
star = 5
for i in range(1,star+1):
     for j in range(1,i+1):
         print('*',end=" ")
     print()
     
* 
* * 
* * * 
* * * * 
* * * * * 

pattern printing using numbers
-------------------------------
star = int(input("enter a number"))
count = 0
for i in range(1,star+1):
     for j in range(1,i+1):
         count+=1
         print(j,end=" ")
     print()

output:
enter a number5
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
------------------------------------------
star = int(input("enter a number"))
count = 0
for i in range(1,star+1):
     for j in range(1,i+1):
         count+=1
         print(j,end=" ")
     print()

output:
enter a number5
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
--------------------------------------------
star = int(input("enter a number"))
count = 0
for i in range(1,star+1):
     for j in range(1,i+1):
         count+=1
         print(count,end=" ")
     print()

output:
enter a number5
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15
---------------------------------------------
'''


star = int(input("enter a number"))
count = 0
for i in range(1,star+1):
     for j in range(1,i+1):
         count+=1
         print(count,end=" ")
     print()

