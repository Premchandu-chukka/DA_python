'''
dictionary
------------


-->Dictionary is a collection of key:value pair
-->key must be unique and it should be immutable datatype
(int,str,tuple)
-->dict is represented by {}
      
      
      data_ = {'name':'prem',
               'balance':7000,
               'adr':123456789,
               'panc':'dfghj7542'}
          print(data_['adr'])
          output:123456789
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Acessing
---------

--> dict can acess by calling key, we will get value from that key

             syntax:dict['key']


             
--> get() is also used to get the value from that key
                  syntax:dict.get['key']
eg:
      data_ = {'name':'prem',
               'balance':7000,
               'adr':123456789,
               'panc':'dfghj7542',
         2:[3,4]}

print(data_['adr'])
print(data_.get(2))

 output: 123456789
         [3, 4] 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



-->update
---------
update  method is used to update key, incase if the key is not present inside dict then it add that key: value
              syntax: dict.update({key:value})
              data_.update({'ac.no':'dfg74185296'})
there is another way
               syntax: dict[key] = value
               data_['AC']=123753963147

               data_ = {'name':'prem',
               'balance':7000,
               'ar':123456789,
               'panc':'dfghj7542',
                       2:[3,4]}

                data_.update({'name':'premchand'})
                print(data_)

                output:123456789
                       [3, 4]
                       {'name': 'premchand', 'balance': 7000, 'adr': 123456789, 'panc': 'dfghj7542', 2: [3, 4]}

                    
           data_.update({'ac.no':'dfg74185296'})
           print(data_)

         output:  123456789
           [3, 4]
           {'name': 'prem', 'balance': 7000, 'adr': 123456789, 'panc': 'dfghj7542', 2: [3, 4], 'ac.no': 'dfg74185296'}

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Values
-------
          
values() method is used to get all  the values from the dict
            syntax:dict.values()
            
           data_ = {'name':'prem',
               'balance':7000,
               'adr':123456789,
               'pan':'dfghj7542',
                'Ac':'dftg74185296'}
                
              print(data_.values())
              output : dict_values(['prem', 7000, 123456789, 'dfghj7542', 'dftg74185296'])
keys
----
keys() method is used to get all  the key from the dict
             syntax:dict.keys()
              data_ = {'name':'prem',
               'balance':7000,
               'adr':123456789,
               'pan':'dfghj7542',
                'Ac':'dftg74185296'}
                print(data_.keys())
              
              output:dict_keys(['name', 'balance', 'adr', 'pan', 'Ac'])



items
----
items() method is used to get both key and value in list one after one
                    syntax:dict.items()
                    
              data_ = {'name':'prem',
               'balance':7000,
               'adr':123456789,
               'pan':'dfghj7542',
                'Ac':'dftg74185296'}
                print(data_.items())
                
                output:dict_items([('name', 'prem'), ('balance', 7000), ('adr', 123456789), ('pan', 'dfghj7542'), ('Ac', 'dftg74185296')])

clear
-----
clear() method is used to clear entire data
         syntax:dict_.clear()

data_ = {'name':'prem',
               'balance':7000,
               'adr':123456789,
               'pan':'dfghj7542',
                'Ac':'dftg74185296'}
                data_.clear()
                print(data_)
                
                output:{}


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

##data_ = {'name':'prem',
##               'balance':7000,
##               'adr':123456789,
##               'pan':'dfghj7542',
##                'Ac':'dftg74185296'}
##
##
###print(data_['adr'])
###print(data_.get(2))
####data_['name']='chandu'
####data_['AC']=123753963147
###data_.update({'ac.no':'dfg74185296'})
##data_.clear()
##print(data_)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Conditions
----------
if statement:
-----------------
--> if condition becomes true, then it will execute inside block of code


    age = 19
if age>=18:
    print('eligible to vote')
print(age)
output:eligible to vote
       19

--> incase it becomes false, it will never enter into inside block of code


      age = 15
if age>=18:
    print('eligible to vote')
print(age)   
output:15
---------------------------------------------------------------------------------------------

if-else
--> else for if statement is a fall back statement, incase if condion fails then else block will execute

age = 15
if age >= 18:
    print(f'your {age}Eligible to vote')
else:
    print(f'your age is {age}years so you have to wait for{18-age} years')
    
    output:your age is 15years so you have to wait for3 years



a = 90
b = 100
if a>b:
    print('a is greater')
else:
    print('b is greater')

output:b is greater
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
##age = 15
##if age >= 18:
##    print(f'your {age}Eligible to vote')
##else:
##    print(f'your age is {age}years so you have to wait for{18-age} years')
##
a = 90
b = 100
if a>b:
    print('a is greater')
else:
    print('b is greater')
