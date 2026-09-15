'''

List
------
-->Collection of different data types that are seperated by, and it is represented by []

Indexing
--------

positive-->0
negative-->-1

           s = [1,2,3,4,"python"]
           print(s[4])
           
            output:python


          s = [1,2,3,4,"python"]
          print(s[4][-2])

             output:o


          all_ = [12,[1,"python",[1,4],(78,[6,7])],["java",78]]
          print(all_[1][3][1])

          output:[6, 7]


len()
--->This function is used to find number of items present inside the list.

            syntax:len(variable_name)
            data_ = ['python',[1,2,(90,'details',[67,0]),(78,'student')]]
            print(len(data_))

            output:2



slicing
------>


              data_ = [1,2,3,4,5,6]
              print(data_[2:6])

              output:[3, 4, 5, 6]

eg:
 a = [1,2]
 b = [3,4]
 print(a+b)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Methods:

append()
--------
It adds the new items at end of the list whenever we append new items to list.
        syntax:variable_name.append(items)
           sp = [1,2]             
           print(sp)
           sp.append(3)
           print(sp)
           sp.append(15)
           print(sp)

           output:[1, 2]
                  [1, 2, 3]
                  [1, 2, 3, 15]

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


extend()
--------
 extend () will add the items into list at last index position but it will give each value as one index inside list

 it cannot accept the non iterables i.e integers
 and it adds each item by splitting
                syntax:variable_name.extend(items)
                 sp = [1,2]
                 print(sp)
                 sp.extend(9)
                 print(sp)
                 output:TypeError: 'int' object is not iterable

                 sp.extend([3,4])
                 print(sp)

                 output:[1, 2, 3, 4]
                 
                 print(sp)
                 sp.extend('python')
                 output:[1, 2, 3, 4, 'p', 'y', 't', 'h', 'o', 'n']


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
pop()
-----
pop is used to remove the item from the list and it will remove the item based on the index position
                 syntax:variable_name.pop(items)
                 sp = [1,2,3,4,'python']
                 sp.pop(3)
                 print(sp)

                 output:[1, 2, 3, 'python']
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
remove()
--------
 oremove() is used to remove the value we need to be removed and it can only remove one value at a time

         syntax:variable_name.remove(value)
         sp = [1,2,3,4,'python']
         sp.remove(3)
         print(sp)

          output:[1, 2, 4, 'python']







'''



sp = [1,2,3,4,'python']
sp.remove(3)
print(sp)







