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
#LECTURE 31 SETS:
#Sets are unordered collection of data, enclosed in curly bracket.
#sets are unchangeable and does not contain duplicate items.
marks = {8,9,6,8,10,4,10}
print(marks)
print(type(marks))
cities = {'karachi','karachi','karachi'}
print(cities)
failures= {} #this is not an empty set vut a empty dict.
print(type(failures))
failed = set() #this is an empty set
print(type(failed))
names = {'ifrah','neha','nabiha','ifrah'}
for name in names: #we can enlist sets elements using for loop
    print(name)
#LECTURE 32 SETS METHOD IN PYTHON:
# UNION,INTERSECTION,SYMMETRIC,DISJOINT,SUBSET,SUPERSET,REMOVE,ADD,DISCARD,DELETE

a = {'icecream','waffle','cookies','chocolate'}
b = {'chocolate','strawberry','icecream','vanilla'}
print(a.union(b))   #adding two sets
print(a)
#a.update(b) #update function will update set a.
#print(a)
print(a.intersection(b))  #taking common
print(a.symmetric_difference(b)) #taking uncommon
print(a.difference(b)) #a-b 
print(b.difference(a)) #b-a

#example#2
area1 = {'nazimabad','north nazimabad','gulshan','bahria town'}
area2 = {'north nazimabad','maymaar','DHA','tariq road'}
print(area1.isdisjoint(area2))#return true if nothing is common else false.
print(area1.issuperset(area2))#return true if set a has all elements of set b
print(area2.issuperset(area1))#return true if set b has all elements of set a
print(area1.issubset(area2))#return true if set a has all elements of set b
print(area2.issubset(area1))#return true if set b has all elements of set a
area1.add('KDA') #add one item only
#area1.update(area2) #by update function u can add a set to another set.
#print(area1)
print(area1)
area1.remove('gulshan') #can remove
print(area1)
print(area1.pop())
print(area2.pop())
#del area1  #this way u can delete an entire set
#print(area1)

#PRACTICE
#You’re given two lists of student names. Find:

#Students in both lists
#Students in only the first list
#Students in both list
list1 = ['Alice', 'Bob', 'Charlie', 'David']
list2 = ['Charlie', 'David', 'Eve', 'Frank']
list3 = set(list1)
list4 = set(list2)
ans1 = list4.union(list3)
print("student in both lists are: ",ans1)
print("students only in list1 are: ",list1)
list5 = list3.intersection(list4)
print("students in both list are: ",list5)

#Check if an Item Exists in a Set
#animals = {"cat", "dog", "rabbit"}
#Ask the user to type the name of an animal.
#Check if that animal is in the set and print "Yes!" or "No!".
animals = {"cat", "dog", "rabbit"}
user = input("enter a animal name: ")
if user=='cat' or user=='dog'or user=='rabbit':
    print("yes")
else:
    print("no")

#    Ask the user to enter a short sentence (e.g., "I love love coding").
#Split the sentence into words.
#Convert the words into a set.
#Print the set (which shows only unique word)
s = input("Enter a sentence: ")
d = s.split()
f = set(d)
print(f)

#Create a set of even numbers from 2 to 10:
#Ask the user to enter a number.
#Check if the number is in the set and print "It's even!" or "Not in the set!".

evens = {2, 4, 6, 8, 10}
num = int(input('enter a number: '))
if num in evens:
    print("it's even!")
else:
    print("not on the set!")

#   Make a set of vowels:
#vowels = {'a', 'e', 'i', 'o', 'u'}
#Ask the user to enter a single letter.
#Use the set to check if it’s a vowel and print the result.
vowels = {'a', 'e', 'i', 'o', 'u'}
letter = input('enter alphabet: ')
if letter in vowels:
    print("Yes it's a vowel!")
else:
    print("it's not a vowel")

#Start with an empty set:
#Ask the user to type something.
#Add it to the set.
#Print the set and say whether it’s empty or not using if.
my_set = set()
your_set= input("you can add anything you want: ")
my_set.add(your_set)
print("set contains ",my_set)
if my_set is ():
    print("null set")
else:
    print("set has elements")


