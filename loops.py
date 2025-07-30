#LECTURE 17 FOR LOOPS:
name = "Ifrah"
for alpha in name: #to iterate
    print(alpha)
list0= ['Ifrah','Obair','Zain']    
for elem in list0: #iterate alements in a list.
    print(elem)
    for letters in elem:
        print(letters) #iterate every single element in the list.
dict0 = {'cs','mbbs','ca','acca'}        
for fields in dict0:
    print(fields)
    for alphabet in fields:
        print(alphabet)
for counting in range(11): # from zero to 10
   # print(counting)        
    print(counting+1)    #from 1 to 11
for numbers in range(1,16):
    print(numbers)    
for num in range(1,12,2): #jump index (jump from 1 -12 at every 2 count)
    print(num)    

#Print the multiplication table of a given number.
#a = int(input("Enter a number: "))
a = 5
for table in range(11):
    print(a,"X",table,"=",a*table)

#Print the factorial of a number using a for loop.
#num = int(input("Enter a positive number: "))
num = 6
factorial = 1
if num<0 :
    print("factorial cannot be calculated of negative integer")
elif num==0:
    print("the factorial of 0 is 1")    
else:
    for k in range(1, num+1):
        factorial *= k
    print(f'The factorial of {num} is {factorial} ')  

#Count the number of vowels in a given string.
university = 'Bahria University'
#vowels = 'a','e','i','o','u','A','E','I','O','U'
vowels = 'aeiouAEIOU'
count = 0
for letters in university:
    if letters in vowels:
       count+=1
print("The total number of vowels in ",university, "is" ,count)
 
 #LECTURE 18 WHILE LOOP:
c = 1
while c<=9:
    print(c)
    c = c +1
print("Done with the loop")
#d = int(input("Enter a number:" ))
#while d<=32:
    #d = int(input("Enter a number:" ))
#print("Done")    

count = 5
while count>0:
    print(count)
    count = count - 1 #decreament while loop!
print("done with dec loop")    

#Print even numbers from 2 to 20 using a while loop.

n = 2
while n<=20:
    print(n)
    n = n + 2
print("These are even numbers from 2-20")

#Take input from the user until they enter 'exit'.
#e = input("Enter: ")
#while e != "exit":
  #   e = input("Enter: ")

#Write a program to find the sum of numbers from 1 to N using a while loop
#f = int(input("Enter a positive integer: ")) #user input
f= 7
totalsum=0
i = 1
while f>=i:
    totalsum+=i
    i+=1
print("The total sum is",totalsum)    

#Write a program that asks the user to guess a number between 1 and 100.
#The program should keep asking until the user guesses the correct number.
#g = int(input("Guess the number: "))
g = 5
while g!= 5:
    g = int(input("Guess the number: "))
    if g!=5 and g>5:
      print("Too High, Try again!")
    elif g!=5 and g<5:  
      print("Too Low, Try again")  
else:
    print("Right guess!")      

#Simulate a basic login system using a while loop (3 attempts allowed).
#print("Enter username and password to sign in")
#count = 0
#while count<3:
#    h = input("Username: ")
#    i = input("Password: ")
#    if h== "ifrah farooq" and i== '9246':
#        print("Access Granted")
#        break
#    else:
#        print("Invalid credentials")
#        count+=1

#LECTURE 19 BREAK AND CONTINUE STATEMENT:
for numbers in range(12):
    print(numbers)
    if numbers== 10:
        break       #this will break the loop at 10
print("out of the loop!")    
for int in range(15):
    if int == 12:
      print("Skip the iteration")
      continue
    print(int)
       

 #LECTURE 35 FOR LOOP:
for i in range (5):
    print(i)
    if i==4:
     break 
else:
    print("sorry no i !)")
i =0
while i<7:
    print(i)    
    i = i + 1
    if i == 6:
        break
else:
    print("end")       
#PRACTICING BREAK AND CONTINUE STATEMENTS:
#Write a Python program to print numbers from 1 to 100, but stop the 
# loop when a number divisible by 17 is encountered.
print("BREAK AND CONTINUE STATEMENT")
for j in range(1,111):
    print(j)
    if j%17==0:
        break
print("Number is divisible by 17")

#Write a program that prints numbers from 1 to 50, but skips the numbers
#  that are divisible by 5 using continue.
for k in range(1,51):
    if k%5==0:
        print("Skipping the num bcs it's divisible by 5")
        continue
    print(k)

#Given a list of numbers, print only the positive numbers using continue.
for l in range(1,30):
    if l%2==1:
        continue
    print(l)
print("evens")    

#Given a list of numbers, use a loop to find if the number 42 exists. 
# If found, print "Found" and break. If not, print "Not found" after 
# the loop.
#CASE 1 (42 NOT PRESENT IN THE LIST)
z = [12,34,55,77,90,3,5,67,87,43,55,22]
for numbers in z[:]:
    #print(numbers)
    if num==42:
        break
else:
     print("42 not found in the list")

x =[12,34,55,77,90,3,5,42,67,87,43,55,22]
for el in x[:]:
    if el==42:
      print("42 is found")
      break
else:
    print("42 cannot be found")
#Write a program that takes a string input and prints only the consonants 
# (skip vowels using continue).
#m = input("enter a sentence: ")
m = "welcome to vscode"
for mm in m :
    if mm in ("aeiouAEIOU"):
        continue
    print(mm)
#Write a program to check if a number is prime using a for loop and break
#when a factor is found.
#prime numbers are the numbers that are greater than one and only divisible by themselves.


    