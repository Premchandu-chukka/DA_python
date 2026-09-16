'''
input()--> input formatting
print()--> output formatting

a,b = 13,4.5
print(a,b)# by default sep =' '
print(a,b,sep=',')
print(9,15,sep=':')
print('codegnan','python','vizag',sep='--->')
# end by default throws new line, we can modify it...
print(a,b,end=' ')
print("codegnan is in vizag",end='\t')
print(' and i travel from my village')

print('---->welcome<----')


a=int(input('enter a number'))
b=int(input('enter a number'))

add=a+b
sub=a-b
mul=a*b
div=a/b
print('addition',add)
print('subtraction',sub)
print('multiplication',mul)
print('divide',div)


a,b = map(int,input("enter the values").split(','))
add=a+b
sub=a-b
mul=a*b
div=a/b
print("=======>calculator<========")
print("allows only+,-,*,/,")
print()
print('addition',add)
print('subtraction',sub)
print('multiplication',mul)
print('divide',div)
print()

#usage of %d,%f,%s
#print("usage of %"%(args))
price = 45.3;grade = 'A';stock = 15
print('%d'%price)
print("%d"%grade)#type error
print("price is %d"%price)
print("price is %f"%price)
print("price is %.1f"%price)
print("price is %s"%grade)

r = 3.5
pi= 3.1416
area = pi*(r)**2
print("area of circle is %.2f"%area)


#new style formatting --> fstring(most recomended after python3.9 version)
name = "codegnan";batch ="DA6"
print(f'{batch} is in {name}')
print(f"prem is in {name}")
'''

#control block statements--> they control the flow of the program
#conditional statements(if,elif,else)
#repetiton statements(loops)(for,while)
#jumping statements(break,continue,pass)
'''
syntax for conditional statements:

if <condition>:
    statement(s)...
    .........
elif  <condition>:
    statement(s)...
    .........
else:
    statement(s)...
    ...........
'''
#BMI converter (body mass index ---> weight,height)(weightin kgs, height in cms,mts)
#height-->feets-->1feet-->12 inches-->1 inch-->2.54cm
#1feet-->30.48cm-->0.3mts
#bmi = weight/((height)**2)


weight = int(input("enter weight in kgs:"))
height = float(input("enter height in meters:"))

##print(bmi)
#now lets divide into categories
'''
<18.5--> underweight
>=18.5 - 24.9--> healthy
>=25 -30--> overweight
>31 --> obesity
'''
if weight>0 and height>0:
    bmi = weight/((height)**2)
    if bmi<18.5:
       print(f"bmi is less than 18.5 and you are underweight --> eat well")
    elif bmi>=18.5 and bmi <24.9:
       print(f"bmi is inbetween 18.5 and 24.9and you are healthy --> eat well and keep consistent")
    elif bmi>=25 and bmi <30:
       print(f"bmi is inbetween 25 and 30and you are overweight --> do some workouts")
    elif bmi>30:
        print(f"bmi is greater than30 and you are with obesity ")
else:
    print("enter only +ve values greater than 0")

#task --> user can enter height in centimeters, feets-->meters
#cal bmi
#make all user validations for height -->cms,feets
#github links

