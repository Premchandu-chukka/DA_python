'''# If the same above BMI scenario we want it to be repeated for specific number of time
# Repetition Statements --> for, while
# for keyword -->
print("---->BMI CALCULATOR<----")

data_={'name' : [],
           'height' :[],
           'weight' : []
           }
n = int(input("enter how many times you want to repeat:"))
for i in range(n):
    
    choice = int(input('enter choice\n1.feet\n2.centimeters\n3.meters :'))
    
    if choice == 1:
        height = float(input('Enter the height in feet:'))
        height = height * 0.3048
        data_["height"].append(height)
        weight = int(input('enter the weight in kgs:'))
        data_["weight"].append(weight)
    elif choice == 2:
        height = float(input('Enter the height in centimeters:'))
        height = height / 100
        data_["height"].append(height)
        weight = int(input('enter the weight in kgs:'))
        data_["weight"].append(weight)
    elif choice == 3:
        height = float(input('Enter the height in meters:'))
        height = height
        data_["height"].append(height)
        weight = int(input('enter the weight in kgs:'))
        data_["weight"].append(weight)
    else:
        print('invalid choice')

    name = input('enter the name:')
    data_["name"].append(name)

    if weight > 0 and height > 0:
        bmi = weight / ((height) ** 2)

        if bmi < 18:
            print(f'bmi of {name} is {bmi} and you are underweight --> Eat well')

        elif bmi >= 18.5 and bmi <= 24.9:
            print(f'bmi of {name} is {bmi} and you are healthy --> keep consistent')

        elif bmi >= 25 and bmi <= 29.9:
            print(f'bmi of {name} is {bmi} and you are overweight --> start Exercising')

        else:
            print(f'bmi of {name} is {bmi} and you are obese')

    else:
        print('enter valid inputs')
print(data_)

'''
#Exception Handling--> exception handling is a mechanism to a program which responds to run time errors or compilations

#Exception --> It tries to make our program go in a normal flow
'''
try,except,finally
try:
    #code that may cause an error...
except:
    #code that handles the error...
finally:


#simple scenario to understand the exception
a,b = map(int,input("enter the values:").split(','))
try:
    result =a/b
    print(result)
except Exception as e:
    print("find it")
    print(e)

# same above case accept inputs in try block

try:
    a,b = map(int,input("enter the values:").split(','))
    result =a/b
    print(result)
except Exception as e:
    print("find it")
    print(e)

#In above case we will get ValueError,ZeroDivisonError...
#Possible types of errors--> TypeError,ValueError,NameError,IndexError,ZeroDivisonError,AttributeError,ArithmeticError
try:
    a,b = map(int,input("enter the values:").split(','))
    result =a/b
    print(result)
except ValueError:
    print("dsgfds fdsghf sgdfdhj dsfgh")
except ZeroDivisionError:
    print("make sure you enter denominator greater than zero")
except NameError:
    print("please understand the syntax")
except AttributeError:
    print("please check  methods or function names properly")
finally:
    print("Exception Handling is completed")

'''
#Multiple Exceptions at a time

try:
    a = [12,3,4,5,6]
    print(a[1])# take one example as print(a[45])
    a.append('data')# take one example as a.appen('data')
    print(a)# take on example as prin(a)
except (IndexError,NameError,AttributeError) as e:
    print(e)
finally:
    print("Done")
