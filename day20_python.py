'''
modules
--------
--> A module is a python file (.py) that written using function, variables, operators, etc.

1. built-in modules
--------------------
--> built in modules are the modules developed by programmer and they come with installation

eg:
-------------------------------
1.math

import math
print(math.pow(2,3))

output:
8.0
-----------------------------
2.os

import os
print(os.getcwd())

------------------------------
3.sys

import sys
print(sys.version)

-------------------------------

4.random

import random
print(random.randint(1000,9999))

output:
9015
------------------------------------------------------------------------------------------
2.user defined modules
----------------------
--> importing specific function from the module
syntax--> from module import function

from batch_da_6 import add_
print(add_(9,15))

    (or)
    
import batch_da_6
print(batch_da_6.pw(15,4))
--------------------------------------

using alias name
----------------

import batch_da_6 as prem_da
print(prem_da.pw(10,9))

'''


import batch_da_6 as prem_da
print(prem_da.pw(10,9))
