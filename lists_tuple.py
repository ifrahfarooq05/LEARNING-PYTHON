#LISTS: #LECTURE 22
marks=[8,9,6,3,0] #index[0:1:2:3:4] #len[5]
print(marks)
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[:])
print(marks[1:4])
print(marks[-3]) #NEGATIVE INDEXING print(marks(len(marks)-3))
                 #                             (5-3) = [2]

print(marks[1:5:2]) #JUMP INDEX                
if 6 in marks:
    print("yes")              
else:
    print("no")   #WE CAN ALSO USE CONDITIONS

list1=[i for i in range(10)]
print(list1)
list2=[i*i for i in range(10)]
print(list2)
list3=[i*i for i in range(10) if i%2==0]
print(list3)
list4=[i*i for i in range(10) if i%2==1]
print(list4)

#LIST METHODS LECTURE 23
l=[43,74,8,12,0,1,43] 
print(l)
l.append(2005) #append: to add a new element in the list.
print(l)
l.sort(reverse=True)#sort: to sort the list followed by the given command.
print(l)
l.reverse()#reverse: ascending order
print(l)
print(l.index(1))#printing the given index.
print(l.count(43))#return the amount a value occurs.
#m=l       #this way the elements of m and l will be equal, and changing 
#m[2]=66   #any element of will change the element of other too.

n=l.copy() #this way n will copy elements of l, and changing element of 
n[1]=6     #any one will not disturb other lists.
print(n)
print(l)
l.insert(1,5)#this way we can change an element of the indec(index,new elem)
print(l)

o = ['eggs','bread','butter']
v = ['wheat','rice','grains']
h= o+v      #we can add two lists.
print(h)
o.extend(v)#another method to add, we can extend a list.
print(o)

#Write a Python program that calculates and prints the sum of 
# all numbers in a list.
 
def calculate_sum(numbers):
   totalsum=0
   for i in numbers:
      totalsum+=i
   print("The sum of all numbers in list is",totalsum)    

kgs=[40,50,45,32,10]
calculate_sum(kgs)
liters=[32.5,81.3,90,43.2]
calculate_sum(liters)
#Write a program to find and print the largest number in a list.
m=[78,90,50,67,82,38]
m.sort(reverse=True)
print(m)
print("The greatest number in the list is",m[0])
#Create a new list that contains the square of each number in the
#  list [1, 2, 3, 4, 5].
list9 =[1, 2, 3, 4, 5]
for i in list9:
    list2= [i*i for i in list9 ]
print(list2)
#Count how many times "apple" appears in the 
# list ["apple", "banana", "apple", "cherry", "apple"].
list_1= ["apple", "banana", "apple", "cherry", "apple"]
print(list_1.count("apple"))

#TUPLE: #LECTURE 24
tup=(12,34,56,78) #tuples are encolsed in round bracket and are immutable.
print(type(tup))
print(tup[0:3])   #we can get index of tuple
print(tup[-2])    #negative indexing
print(tup[0:3:2]) #jump index
if 56 in tup:
    print("true")  #we can aslo check the elements by using if else statements.
else:
    print("false")
if 89 in tup:
    print("true")    
else:
    print("false")
for i in tup:
    print(i*i)    #getting squares of each elememt
for i in tup:
    print(i*2)    #we can perform arithmetic operations.
tup2= (tup + (12,3,44,65))    
print(tup2)       #we can not modify exisiting tuple but can add elements to other tuples.
tup3= tup+tup2    # we can add two tupes by creating another tuple.
#/we cannot append, sort, reverse,chang index aur modify a tuple/#
#TUPLE METHODS #LECTURE 25
#write a program consiting of tuple and make changes to that tuple.
countries=("Russia","Pakistan","Palestine","Austria","America")
item = list(countries)  #converts a tuple into list
item.append("Canada")   #add new element
item.pop(3)             #remove existing element
item[2]="United Kingdom"#swtich element
countries=tuple(item)   #covert the list into a tuple
print(countries)
#EXAMPLE OF TUPLE FUNCTIONS:
scores= (87,76,56,98,32,45,66,89,98)
print(scores.count(98))
print(scores.index(56))
print(scores.index(32,4,8)) #slicing 4-8 to find 32

#Write a function that takes a tuple of numbers and returns the sum
#  of all even numbers.
def calculate_sum_even_no (abc):
 totalsum=0
 for i in  (abc):
    if i%2==0:
        print(i+i)
        totalsum+=i
 print("The sum of all even numbers in the list is : ",totalsum)        
integers=(43,56,9,8,12,66,9,42)
calculate_sum_even_no(integers)

points=(33,55,8,63,21)
calculate_sum_even_no(points)
#Write a program to merge two tuples and remove duplicates.
T1=("grains","wheat","cotton","grains","rice")
T2=("cream","milk","butter","milk","yogurt")
L1= list(T1)
L2= list(T2)
L3= L1 + L2
print(L3)
L4= set(L3)
print(L4)