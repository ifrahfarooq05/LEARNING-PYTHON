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