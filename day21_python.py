'''
math
----
import math
print(math.pi)
print(math.ceil(4.3))
print(math.floor(5.6))
print(math.sqrt(25))
print(math.sin(2))
print(math.pow(2,3))
print(math.cos(5))

outcomes:
3.141592653589793
5
5
5.0
0.9092974268256817
8.0
0.28366218546322625

random
-------
import random
print(random.randint(100000,999999))
print(random.randrange(1,100))
color = ['blue','green','red','white','orange']
print(random.choice(color))
random.shuffle(color)
print(color)

outcomes:
425960
54
red
['blue', 'green', 'orange', 'red', 'white']

platform
--------
import platform
print(platform.system())
print(platform.python_version())
print(platform.platform())
print(platform.processor())

outcomes:
Windows
3.12.9
Windows-11-10.0.26200-SP0
AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD

collections
----------
import collections
data_ = ['banana','mango','apple','orange','orange','banana']
print(collections.Counter(data_))
all_ = collections.Counter(data_)
print(all_.most_common())

outcomes:
Counter({'banana': 2, 'orange': 2, 'mango': 1, 'apple': 1})
[('banana', 2), ('orange', 2), ('mango', 1), ('apple', 1)]


from collections import defaultdict
data_ = defaultdict(list)
data_['python'].append('prem')
data_['python'].append('chand')
data_['java'].append('pc')
print(data_)


from datetime import datetime
today = datetime.today()
now = datetime.now()
print(today.month)
print(today.day)
print(today.year)
print(today.hour)
print(today.minute)

outcome:
9
7
2026
14
42

from datetime import datetime
now = datetime.now()
print(now.strftime('%d-%m-%y'))
print(now.strftime('%H:%M:%S'))
print(now.strftime('%a'))

outcome:
07-09-26
14:47:09
Mon


import random
attempt = 3
num = random.randrange(1,100)
print(num)
while attempt > 0:
    game = int(input('enter a number between 1 and 100'))
    if game == num:
        print("your guess is correct")
        break
    else:
        attempt -= 1
        print("your guess is not correct")
        print(f'{attempt}  attempts  left')
if attempt == 3:
    print('price money is 500')
elif attempt == 2:
    print('price money is 300')
elif attempt == 1:
    print('price money is 100')
else:
    print('better luck next time')

output:
35
enter a number between 1 and 10023
your guess is not correct
2  attempts  left
enter a number between 1 and 10053
your guess is not correct
1  attempts  left
enter a number between 1 and 10035
your guess is correct
price money is 100


import itertools
a = itertools.count(45)
print(next(a))
print(next(a))
b = itertools.repeat('python',6)
for j in b:
    print(j)
c = itertools.cycle(['python','java','c'])
for j in range(5):
    print(next(c))

outcome:

45
46
python
python
python
python
python
python
python
java
c
python
java

n = itertools.chain([1,2,3],[4,5,6])
for i in  n:
    print(next(n))

'''
import itertools
a = itertools.count(45)
print(next(a))
print(next(a))
b = itertools.repeat('python',6)
for j in b:
    print(j)
c = itertools.cycle(['python','java','c'])
for j in range(5):
    print(next(c))
n = itertools.chain([1,2,3],[4,5,6])
for i in  n:
    print(next(n))
