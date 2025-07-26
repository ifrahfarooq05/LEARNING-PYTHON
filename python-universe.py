#LECTURE 28- f STRINGS IN PYTHON:
name = "Ifrah"
country = "Pakistan"
print("Hey My name is {name} and I am from {country}")
#without using f strin it will print it as it is, but if we use f string 
#it will input name and country from the variable data.
print(f"Hey My name is {name} and I am from {country}")
price = 76.9876 
print(f"I bought a pair of shoes in only {price:.3f} dollars")
print ("{2*8}")# it appears as a string due to ("")
print(type(f"{2*8}"))#it's a string too, but gives integer answer.
#Any valid Python expression can be placed within the curly braces, 
# including variable names, arithmetic operations, function calls, and more.
# F-strings support advanced formatting options using a colon :
#  followed by a format specifier within the curly braces. 
# This allows for control over things like precision, alignment, padding etc

#LECTURE 29 DOCS.STRINGS
#DOCS.STRINGS ARE JUST DESCRIPTION OF GIVEN FUNCTION
def square(n):
    '''Takes a number n and returns the square of n'''
    print(n*n) 

square(9)
print(square.__doc__)

def name(a):
    '''Takes name from user and return it's length'''
    print(len(a))

name("Ifrah")
print(name.__doc__) #it describes a program better!!


