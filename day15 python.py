'''
reversing the string
-------------------
words = "madam"
empty_str = " "
for i in words:
    empty_str = i + empty_str
    print(empty_str)

output:
m 
am 
dam 
adam 
madam
-------------------------
    
words = "madam"
empty_str = " "
for i in words:
    empty_str = i + empty_str
if empty_str == words:
    print(f"{words} is palindrome")
else:
    print(f"{words}is not palindrome")


output:madamis not palindrome
--------------------------------------------------------------------------------------------

Armstrong number
------------------

num = int(input("enter a number:"))
length_ = len(str(num))
armstrong = 0
for i in str(num):
    armstrong = armstrong + int(i)**length_
##    print(armstrong)
if armstrong == num:
    print(f"{num} is armstrong number")
else:
    print(f"{num} is not a armstrong number")

output:
enter a number:153
153 is armstrong number
--------------------------------------------------------------------------------------------

Perfect number
--------------

num = int(input("enter a number:"))
sums = 0
for i in range(1,num):
    if num % i == 0:
        sums += i
if sums == num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")

output:
enter a number:28
28 is a perfect number

enter a number:18
18 is not a perfect number
--------------------------------------------------------------------------------------------

fibonacci series
----------------


num = 0
num_2 = 1
print(num,num_2,end=" ")

for i in range(1,10):
    num_3 = num + num_2
    num =num_2
    num_2 = num_3
    print(num_3,end=" ")

output:

'''
num = 0
num_2 = 1
print(num,num_2,end=" ")

for i in range(1,10):
    num_3 = num + num_2
    num =num_2
    num_2 = num_3
    print(num_3,end=" ")
    
   
    
    

