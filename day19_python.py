'''
list comprehension
------------------
--> list comprehension is the shortest form of syntax to create a list
-->syntax 1 --> [expression loop condition]
-->syntax 2 --> [expression  condition else loop]

old_ = (1,2,3,4,5,6)
new_ = [i for i in old_ if  i%2 == 0]
print(new_)

output:
[2, 4, 6]


old_ = (1,2,3,4,5,6)
new_ = [i if  i%2 == 0 else None  for i in old_]
print(new_)

output:
[None, 2, None, 4, None, 6]
--------------------------------------------------------------------------------------------
nested comprehension
--------------------
--> using list comprehension generating list inside list


any_ = [[i*j for i in range(1,6)] for j in range(1,10)]
print(any_)

output:
[[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25], [6, 12, 18, 24, 30], [7, 14, 21, 28, 35], [8, 16, 24, 32, 40], [9, 18, 27, 36, 45]]

abc = [[1,2,3],
      [4,5,6],
      [7,8,9]]
data_ =[num for i in abc for num in i]
print(data_)

output:
[1, 2, 3, 4, 5, 6, 7, 8, 9]
---------------------------------------------------------------------------------------------
generator
---------
--> a generator is a special function which generate one value at a time

def all_():
    for j in range(1,10):
        yield j
j = all_()
print(next(j))
print(next(j))

'''
def all_():
    for j in range(1,10):
        yield j
j = all_()
print(next(j))
print(next(j))
