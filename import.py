#LECTURE 44 IMPORT IN PYTHON:
import math
print(math.sqrt(49)) 
import math as m       #can import with another name
print(m.pi*(2))
from math import factorial  #can import only the function we need
print(math.factorial(4))
import math 
print(dir(math)) # by using dir function we can get all the availabe functions of what we imported
print(math.lcm(40))
print(math.lcm, type(math.lcm)) #we can also find the type.
from prac_questions import even_index #can import from our files too.
