'''
print('b=',b)



Datatypes  & TypeConversions
----------------------------
1.Numeric Datatype
------------------
--->Float and integer is called as numeric datatypes

--->Float : A number which contains decimal values, we call it as a float datatype
eg:
price = 56.89

--->Integer(int) : A normal number without any decimal values 
eg:
num = 89
num_2 = 15
----------------------------------------------------------------------------------------

2.String
---------
---> String is a sequence of character that are enclosed in '',"",""""""
eg:
any_ = 'Python is a language'
all_ = 'Ab,.&[)-+'
String is immutable
------------------------------------------------------------------------------------------

3.List
---------
---> List is a collection of different datatypes
--->It is represented by [] that are separated by ,
--->inside the list we call it as items
--->list is mutable
eg:
any_ = [1,'Python',[7,9]]
print(type(any_))
--------------------------------------------------------------------------------------------

4.Tuple
----------
--->Tuple is a collection of different datatypes
--->It is represented by () that are separated by ,
---> It is immutable
eg:
nums = (1,2,3.14,'python',[7,9],(10,4))
---------------------------------------------------------------------------------------------

5.Dictionary 
------------
--->Dictionary is a key:value pairs, keys and values are separated by :
--->Key and value pair is called as item and these items are separated by ,
---> Dictionaries is represented by curly braces {}
---> In keys place we can use immutable datatypes
---> In values place we can use mutable datatypes 
eg:
data_ = {1:2,
          'name':'prem',
           (4,10):'chand'}
print(data_)
----------------------------------------------------------------------------------------------

6.Set
---------
--->Set is a collection of unique elements and sets cannot allow any duplicate values inside it...
---> Set is represented by {} and elements are separated by ,
an = {1,2,3}
print(an)



---------------------------------------------------
Type conversion
--------------

float--> int, str

eg--> int()
price = 45.45
print(int(price))

eg--> str()
price = 45.45
con = str(price)
print(type(con))
-----------------------------------

int-->float, str

num = 78
print(float(num))


eg--> str()
num = 10
con_ = str(num)
print(float(do))


-------------------------------

str--> int, float

eg-->int()
do = '3456'
print(int(do))

eg--> str()
do = '10.04'
print(float(do))
-------------------------------

list--> tuple, string
eg--> tuple()
nums = [1,2,3,4]
print(tuplke(nums))


-->str()


tuple---> list
eg--> list()
all_ = (1,2,3)
print(list(all_)

set-->tuple,list
eg--> tuple()
all_ = {4,5,6}
print(tuple(all_))


dictionary--> list
eg--> dict()
details = [('name','prem'),('edu','b.tech')]
print(dict(details))








'''