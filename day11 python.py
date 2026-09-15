'''

elif
-----
-->elif statements is used to chech more possible outcomes or more condions

a=15
b=170
c=50
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else :
    print(c)

output:170
--------------------------------------------------


num = 9
num_2 = 15

user_opt = int(input('enter \n1.add \n2.sub \n3.mul \n4.pow:'))
if user_opt == 1:
    print(num+num_2)
elif user_opt == 2:
    print(num-num_2)
elif user_opt == 3:
    print(num*num_2)
else:
    print(num**num_2)

output:enter 
1.add 
2.sub 
3.mul 
4.pow:1
24
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

nested if
---------
-->if inside if statement is called nested if

import random

app_details = {'pin': 1234}

user_pass = int(input("Enter your app password: "))

otp = random.randint(1000, 9999)

if user_pass == app_details['pin']:
    print("Password is correct")
    print("Your OTP is:", otp)

    user_otp = int(input("Enter 4 digit OTP: "))

    if user_otp == otp:
        print("Welcome to the app")
    else:
        print("Incorrect OTP")
else:
    print("Password is incorrect")



output:
Enter your app password: 1234
Password is correct
Your OTP is: 4072
Enter 4 digit OTP: 4072
Welcome to the app

----------------------------------------------------------------------------------------
gradding system:


marks_= int(input("enter your marks:"))
if marks_ >=90:
            print('A+')
elif marks_ >=80:
            print('A')            
elif marks_ >=70:
            print('B+')
elif marks_ >=60:
            print('B') 
elif marks_ >=50:
            print('c+')
else:
    print('candidate is fail')

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



'''

marks_= int(input("enter your marks:"))
if marks_ >=90:
            print('A+')
elif marks_ >=80:
            print('A')            
elif marks_ >=70:
            print('B+')
elif marks_ >=60:
            print('B') 
elif marks_ >=50:
            print('c+')
else:
    print('candidate is fail')
            

            
