'''
sets and set operations
-----------------------------


Set
---
-->Set is un ordered collection of elements
-->no duplicates allowed in the set
-->set is represented by{}
eg:
    nums = {1,2,3,4,}
    print(nums)



operations
------------

union()
------
--> the union()will combine two sets into single set
        syntax:set_1.union(set_2) or set_1 | set_2
        data = {1,2,3,4}
        nums = {5,6,7,8,9}
        print(data.union(nums))
        output:{1, 2, 3, 6, 7, 8, 9}




intersection()
------------
--> the intersection will give common elements from both sets

            syntax:set_1.intersection(set_2) or set_1 & set_2
            data = {1,2,3,6}
            nums = {2,6,7,8,9}
            print(data.intersection(nums))
            output:{2, 6}
            


difference()
-----------
--> it will display difference elements from set1 but not from set2 elements

               syntax:set_1.difference(set_2) or set_1 - set_2
               data = {1,2,3,6}
               nums = {2,6,7,8,9}
               print(data.difference(nums))
               output: {1, 3}
               

symmetric_difference()
--------------------
--> it will display difference values from both sets

                syntax:set_1.symmetric_difference(set_2) or set_1 ^ set_2
                data = {1,2,3,6}
                nums = {2,6,7,8,9}
                print(data.symmetric_difference(nums))
                output:{1, 3, 7, 8, 9}

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                
Methods:
--------

-->add() method will add only one element at a time
               syntax:set.add(elements)
               data = {1,2,3,6}
               data.add(9)
               print(data)
               output:{1, 2, 3, 6, 9}



-->update() method will add multiple elements at a time               

                  syntax:set.update([elements]) or set_1.update(set_2)
                  data = {1,2,3,6}
                  data.update([9,5,4])
                  print(data)
                  output:{1, 2, 3, 4, 5, 6, 9}


-->remove() method will delete the given element from the set, and if the given element is not available in set it will raise error

                 syntax:set.remove(elements)
                 nums = {2,6,7,8,9}
                 nums.remove(6)
                 print(nums)
                 output:{2, 7, 8, 9}
                 
-->discard() method is used to delete the elements from the set, but it wont raise any error if the given element is not available in the set


                syntax:set.discard(elements)
                 nums = {2,6,7,8,9}
                 nums.discard(7)
                 print(nums)
                 output:{2, 6, 8, 9}


-->clear() method is used to delete entire elements from the set and it will written empty set i.e set()

                 syntax:set.clear(elements) 
                 nums = {2,6,7,8,9}
                 nums.clear()
                 print(nums)
                 set()
'''
data = {1,2,3,6}
nums = {2,6,7,8,9}
nums.clear()
print(nums)
#print(data.symmetric_difference(nums))
