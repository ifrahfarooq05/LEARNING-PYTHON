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


#CREATING A GENERAL KNOWLEDGE QUIZ: EXERCISE 3
Q1 = str( '''What is the capital city of Canada?
A) Toronto
B) Ottawa
C) Vancouver
D) Montreal ''')
Q2 = str( '''Who wrote the play Romeo and Juliet?
A) Charles Dickens
B) William Shakespeare
C) Jane Austen
D) George Bernard Shaw''')
Q3 = str('''What is the largest planet in our solar system?
A) Earth
B) Saturn
C) Jupiter
D) Neptune''')
print(' "WELCOME TO QUIZ-WHIZZ WITH IFRAH" ')
print( 'Test your brainpower and boost your knowledge with Ifrah’s ultimate quiz challenge!')
print(' " ANSWER THE QUESTIONS AND WIN PRIZES" ')      

print(Q1)
a = input("Your answer: ")
if a=="ottawa":
    print("Correct answer u win 10,000 Rupees")
else:
    print("Wrong answer,Correct answer is Ottawa ")
print(Q2)    
b = input("Your answer: ")
if b=="William Shakespeare":
    print("Correct answer, u win 10,000 Rupees")
else:
    print("Wrong Answer, correct answer is William Shakespeare")
print(Q3)    
c = input("Your Answer: ")
if c== "Jupiter":
    print("Correct answer, u win 10,000 Rupees")
else:
    print("Wrong Answer, Correct answer is Jupiter")


