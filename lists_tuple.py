#LISTS
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

#LIST METHODS
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
list =[1, 2, 3, 4, 5]
for i in list:
    list2= [i*i for i in list ]
print(list2)
#Count how many times "apple" appears in the 
# list ["apple", "banana", "apple", "cherry", "apple"].
list= ["apple", "banana", "apple", "cherry", "apple"]
print(list.count("apple"))
