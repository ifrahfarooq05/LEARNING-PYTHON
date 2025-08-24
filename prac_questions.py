#finding all prime numbers till n(user input):
#When checking if a number is prime, you only need to check for divisibility up to its square root, not all the way up to the number itself.
def prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True    

#a = int(input("Enter a number: "))
a= 20
print(f"Prime numbers upto {a}: ")        
for i in range(2,a+1):
    if prime(i):
        print(i, end=',')

#Print numbers from 1 to 50, but skip numbers divisible by 3. 
for n in range(1,51):
    if n%3==1:
        print(n)

#Ask the user to enter a word and print:
#The word in uppercase #The first and last letter #The word in reverse
#Count how many times the letter 'a' appears in a string.
def print_str (s):
    print(s.upper())#uppercase
    print(s[0]) #first letter
    print(s[-1])#last letter
    print(s[::-1])#reverse text
    print(s.count('a'))#count a

#b = input("Enter a sentence: ") 
#print_str(b)   

#Create a list of 5 numbers and print:
#The length  #The first and last number  #The sum of all numbers.
#Replace the third item in a list with "hello" and print the updated list.
def my_list(l):
    c= len(l)
    d= l[0]
    e= l[-1]
    f= l.insert(3,'hello')
    print("The length of the list is ",c)
    print("The first element of the list is", d)
    print("The last element of the list is ",e)
    print(l)

def my_sum(integers):
    totalsum=0
    for n in integers:
        totalsum += n
    print("The total sum of all numbers in the list is ", totalsum)
    

list1=[22,34,55,67,8]
my_list(list1)
list2=[22,34,55,67,8]
my_sum(list2)

#Write a program that swaps the value of two variables
def swap (a=1,b=2):
    print("Before swap: ")
    print("value 1 =",a, "value 2 =",b)
    a,b= b,a
    print("After swap: ")
    print("value 1 =",a, "value 2 =",b)
    

n1= 5
n2= 8
swap(n1,n2)    
ifrah = 10
gumiho = 0
swap(ifrah,gumiho)

#Write a function to check whether a string is a palindrome 
# (reads the same forwards and backwards).
def check_palin (o):
    try:
     if o==(o[::-1]):
      print(f"The word {o} is palindrome")
     else:
         print(f"The word {o} is not palindrome")
    except Exception as e:
        print(e)
            

car = "civic"
check_palin(car)
name="ifrah"
check_palin(name)
time= "noon"
check_palin(time)

#Write a function that takes a number and returns the sum of its digits.
#a= 12 ans=3
def sum_of_digits(u):
    total = 0
    while u > 0:
        total += u % 10    
        u = u // 10        
    print(f"The sum of digits  is {total}")

no1= 123
sum_of_digits(no1)        
no2= 45
sum_of_digits(no2)

# Write a function that counts how many vowels are in a given string.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

mobile = "samsung"
print(count_vowels(mobile))
name= 'ifrah'
print(count_vowels(name))

#short if else statement
#Write a short if-else statement to check if a number is even or odd.

def is_oddoreven (u):
    print('even') if u%2==0 else print("odd")

#evenodd=int(input("enter a positive integer: "))
#is_oddoreven(evenodd)

#Use nested short if-else to classify a number.
def classify (i):
    print("positive") if i>=0 else print("negative")
#clas=int(input("enter a number: "))    
#classify(clas)

#Check if a person is eligible to vote (age ≥ 18).
def canvote (p):
    print("eligible")if p >=18 else print("underage")
#age= int(input("Enter your age: "))    
#canvote(age)
                   
#ENUMERATE FUNCTION IN PYTHON:
marks = [12,33,45,67,89,67,90]  
for index, mark in  enumerate(marks, start=1):
    print(mark)
    if (index==4):
        print("there we go!")  

vegeis = ("capcicum","pea","carrot","cabbage","potatoe","tomatoe")    
for index, veg in enumerate(vegeis)  :
    print(veg)
    if(index==3):
        print("This is 4th in the list")

students=['ali','taha','fahad','zain','ubair','soha','neha','ifra']  
student_list=[]
for index, student in enumerate(students,start=1):
   student_list.append(f"{index}:{student}")  
print (student_list)

#Write a function that takes a list of integers and returns a new list containing only the numbers that are at even indexes.

def even_index(a):
    for index,i in enumerate(a):
        if (index%2==0):
            print(i)
            
numbers=[12,21,33,48,5,62,73,81,92,0]
even_index(numbers)

#Write a program to: Print any number from 1 to 100. Print the sum of numbers from 1 to n.
def sumnum (m):
    try:
        sumcount=0
        e= int(input("Enter a number : "))
        for numbers in range(e+1):
            sumcount+=numbers
        print(f"The sum of all numbers from 1 to {e} is {sumcount} ")
    except Exception as error:
        print(e)

hello= "call"
#sumnum(hello)

#Create a list of 5 numbers. Print the max, min, and average of the list.
list05=[3,22,15,3,5]
print (f"The max number in the list is {max(list05)}")
print(f"The max number in the list is {min(list05)}")
avg= sum(list05)/len(list05)
print(f"The average is {avg}")

#Write a function that: Takes a list of numbers as input. Returns the second largest number.
def sec_larg(jasmine):
    try:
        rose = list(set(jasmine))
        rose.sort(reverse=True)
        print(rose[1])

    except Exception as oo:
        print(oo)    
            
sun = [11,22,33,44,55]
sec_larg(sun)    

#Check if a string is a palindrome.Count the number of vowels in a string.
def checkingstr (potatoes):
    try:
        if potatoes==potatoes[::-1]:
            print("The string is palindrome")
        else:
            print("The string is not a palindrome")
        count=0    
        vowels="aeiouAEIOU"
        for potatoe in potatoes:  
            if potatoe in vowels:
             count+=1
        print (f"Total vowels in {potatoes} is {count}")    
    except Exception as l:
        print(l)   

spinach = "civic"
checkingstr(spinach)

#Print numbers from 1 to 100. For multiples of 3 print "Fizz", for multiples of 5 print "Buzz", and for both print "FizzBuz".
for numbers in range(1,101):
    print(numbers)
    if numbers%3==0 and numbers%5==0:
        print("fizz buzz")    
    elif numbers%3==0:
        print("fizz")
    elif numbers%5==0:
        print("buzz")

#Write a function that checks if two strings are anagrams.
def anagram_check(str1,str2):
    if sorted(str1)==sorted(str2):
        print(f"{str1} and {str2} are anagrams")
    else:
        print(f"{str1} and {str2} are not anagrams")

s ="silent"
l ="listen"
anagram_check(s,l)
g = "world"
h = "earth"
anagram_check(g,h)
k = "elite"
j = "litee"
anagram_check(k,j)