'''

Strings
-------------
Operations
----------
1.Indexing
--> Indexing is used to get char that you looking to access types

        1.Positive indexing- starts from 0index
         syntax-->print(variable_name[index_position]

          ex: text = 'python' # positive index
          print(text[4])

          output:o
---------------------------------------------------------------
2.Negative indexing- starts from -1index
        syntax-->print(variable_name[Negative index_position]


      eg: text = 'python' # Negative index
          print(text[-2])

         output:o

task
------
txt = 'python is a programming language'
print(txt[17])
output:a
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 len(): it is a built in function that is used to get number of char present in the given string
        syntax: len(variable_name)
        
        txt = 'python is a programming language'
        print(len(txt))
        
        output:32
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 slicing: It is used to acess the particular part from the string
         syntax: print(variable_name[start:end])


        txt = 'python is a programming language'
        print(txt[12:23])
       output: programming
        
        txt = 'python is a programming language'
        print(txt[:23])
      output:  python is a programming

        txt = 'python is a programming language'
        print(txt[12:])
       output: programming language
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
upper(): It is used to convert a all small chars in string into capital letters
        syntax: print(variable_name.upper())
        
        txt = 'python is a programming language'
        print(txt.upper())
        output:  PYTHON IS A PROGRAMMING LANGUAGE


lower(): It is used to convert a all capital letters chars in string into lowercase
          syntax: print(variable_name.lower())
          
          txt = 'PYTHON IS A PROGRAMMING LANGUAGE'
         print(txt.lower())
         output: python is a programming language
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 index() :It is used to know the index position of a char
          syntax: print(variable_name.index('substring',start,end))

           txt = 'python is a programming language'
           print(txt.index('l'))
          output: 24

          
           txt = 'python is a programming language'
           print(txt.index('i',9))
           output:20
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
replace() : It is used to replace old substring with new substring
            syntax: print(variable_name.replace('python', 'java'))

            txt = 'python is a programming language'
            print(txt.replace('python', 'java'))
            output:java is a programming language
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
split() :This is method used to seperate the string based on given substring
         syntax:print(variable_name.split('substring'))

         txt = 'python is a programming language'
         print(txt.split('n'))
        output:['pytho', ' is a programmi', 'g la', 'guage']


        txt = 'python is a programming language'
        a =txt.split(' ')
        print(a)
        print(len(a))

        output:['python', 'is', 'a', 'programming', 'language']
         5
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
count() :It is used to count number of occurances of an substring
        syntax:print(variable_name.count('substring',start,end)

        txt = 'python is a programming language'
        print(txt.count('a',1,20))
        output:2
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



'''

txt = 'python is a programming language'
a = txt[12:23]
print(a)   

if a == a[::-1]:
    print("palindrome")
else:
    print("not a palindrome")
