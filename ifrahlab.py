#while loop
a = 1
while(a<=6):
    print(a)
    a = a+1
b = 2
while(b<24):
    print(b)
    b = b*2
d = 5
while(d>0):
    print(d)
    d = d-2
else:
    print("DONE")
for i in range(12):
    print("5 X",i,"=",5*i)
    if (i == 6):
        break
print("skip the loop")
for k in range(10):
    if k == 8:
        print("skip")
        continue
    print("2 X",k,"=",2*k)
for j in range(12):
    if j == 5:
     print("skip the iteration")
     continue
    print("2 X",j,"=",2*j)
name = "123"
for i in name :
    print(i)
    if i == 2:
        break
print("end")
    # write a program that takes a number (n) from the user and 
    #print how many even and odd numbers are btwn 1 and n.

#QUES 1 
numbers= [1,3,4,7,10,32,41,65,11]
even_count=0
odd_count=0
for num in numbers:
    if num%2==0:
        even_count+=1 
    elif num%2==1:
        odd_count+=1
print("no of even numbers:",even_count)
print("no of odd numbers:",odd_count)
#QUES2
integers=int(input("enter a number: "))
even_count=0
odd_count=0
for k in range(0,integers):
    if k%2==0:
        even_count+=1
    else:
        odd_count+=1
print("the no of even numbers:",even_count)
print("the no of odd numbers:",odd_count)
#write a program that takes a number from the user and print whether its even 
#or odd.
k = int(input("enter a number: "))
if k%2==0:
    print("even")
else:
    print("odd")
    #ask the user for input(n)and print the sum of all num from 1 to n.
count = int(input("How many numbers do you want to sum? "))
total_sum = 0
for i in range(count):
        num = float(input(f"Enter number {i + 1}: "))
        total_sum += num
        continue
print(f"The sum of all numbers is: {total_sum}")
#Take two num and an operator (+,-,*,/)as an input and perform the operation
h = int(input("enter your first number: "))
p = int(input("enter your second number: "))
print ("the sum of numbers is: ",(h+p))
print ("the sub of numbers is: ",(h-p))
print ("the multiplication of numbers is: ",(h*p))
print ("the division of numbers is: ",(h/p))
#take a num as an input and print its multiplication table upto to 10
s = int(input("enter a number: "))
for k in range(1,11):
    print(f"{s} x",k,"=",s*k)
  #ask user to print a num print wether its pos, neg, or zero.
a = int(input("enter a number: "))
if a>0:
    print("number is positive")
elif a<0:
    print("number is negartive")
else:
    print("number is zero")

    #STRINGS FUNCTION PRACTICE SELF
a = "Bahria University!"
print(a.upper())
print(a.lower())
print(a.startswith("B"))
print(a.endswith("y"))
print(a.strip())
print(a.rstrip("!"))
print(a.swapcase())
print(a.islower())
print(a.isupper())
print(a.capitalize())
print(a.count("a"))
print(a.istitle())
print(a.isalpha())
print(a.isalnum())
print(a.find("w"))
print(a.replace("B", "m"))
print(a.isspace())
print(a.split())
print(a.swapcase())
print(a.title())
print(a.center(25))
#ANOTHER EXERCISE TO MEMORIZE STRINGS.
b = " 'birth date is 05 september'!"
print(b.upper())
print(b.lower())
print(b.strip())
print(b.rstrip("september'!"))
print(b.capitalize())
print(b.center(20))
print(b.isupper())
print(b.islower())
print(b.isspace())
print(b.swapcase())
print(b.replace("05" , "09"))
print(b.istitle())
print(b.isalnum())
print(b.isalpha())
print(b.find("s"))
print(b.split())
print(b.startswith("'"))
print(b.endswith("!"))
print(b.count("e"))
print(b.title())
print('Enter correct username and password combo to continue')
count=0
while count < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password=='9246' and username=='ifrah farooq':
        print('Access granted')
        break
    else:
        print('Access denied. Try again.')
        count += 1
#RANDOM PRACTICE TO BOOST LEARNING     
print( 45+67)
print("ifrah you are the best\nand others are not better than you")
#hey ifrah best pf luck for your future
print("hello world")#this is how things work!
print(45+78)
print ("Ifrah is wonderful")
'''
day 2 of learning python
video no 05
'''
print("i am a \"good girl\"\nand she is also a good girl")
print("hey", 8,7,sep= "!")
print("hey",8,9, sep= "~",end="009/n")
print("IFRAH")
print("hey ifrah how are you" , 876, 78, sep= " -", end= "OF/n")
print("i am fine")
print("IFRAH")
print(56*90)
#hey beautiful
'''
i m fine
hey how are you
'''
print("hey how are you\nand where u have been these days")
print("her nsme is \" ifrah\"and she is pretty")
print(" there are many fruits in the basket for example, bananas, apples, oranges, sep= ","")
a=1
a1=9
print(a)
print(a1)
print(a+a1)
b= complex(8,2)
print(b)
c= "True"
d= None
print(c)
print(d)
print("The type of a is ", type(a))
print("The type of b is ", type(b))
print("The type of c is ", type(c))
print("The type of c is ", type(d))
dict1 = {"name": "ifrah" , "age":19, "canvote": True}
print("dict1")
print(15+3)
print(15-3)
print(15/3)
print(15//3)
print(15%3)
print(15**5)
n = 15
m = 7
ans1 = n+m
print("Addition of" ,n, "and" ,m,"is" , ans1) 
ans2 = n-m
print("Subtraction of" ,n,"and" ,m,"is", ans2)
ans3 = n*m
print("Multiplication of", n, "and",m,"is", ans3)
ans4 = n/m
print("Division of" ,n, "and", m,"is", ans4)
ans5 = n%m
print("Modulus of" ,n, "and",m, "is", ans5)
ans6 = n//m
print("Floor division of", n, "and" , m, "is" , ans6)
a = "1"
b =" 5"
print(a + b)
c = "ifrah"
d = " farooq"
e = 1
f = 5
print (c + d)
print( e + f)
print(int(a) + int(b))
w = 9.1
x = 5
print(x+w)
#a = input("enter your name: ")
#print
#= input(" enter first number: ")
#= input("enter second number: ")
#rint(int(b) + int(c))
#again making calculator
l = 2
m = 4
print("Addition of",l, "+",m, "is", l+m)
print("subtraction of",l, "-",m, "is", l-m)
print("multiplication of",l, "*",m, "is", l*m)
print("modulus of",l, "%",m, "is", l%m)
print("division of",l, "/",m, "is", l/m)
print("my name is ifrah \nand i am 20 old")
a = "5"
b = "7"
print(a + b)
print(int(a)+int(b))
# "irah farooq"
#= "20"
#rint("her name is" ,c, "and her age is" ,d)
#rint(c +d)
#= input("My name is:" )
## input("and my age is:" )
#rint(h +f)
#rint("My name is" ,h, "and my age is" ,f, )
# = input()
# = input()
#rint(int(v)+int(z))
#int(int(v)-int(z))
#rint(int(v)*int(z))
#rint(int(v)/int(z))
#rint(int(v)%int(z))
a = 1
b = True
c = 12.5
d = "ifrah "
print("the type of a is", type(a))
print("the type of b is", type(b))
print("the type of c is", type(c))
print("the type of d is", type(d))
name = "ictoria"
age = 25
print(name)
print(age)
apple = 'He said, "i eat an apple"'
print(apple)
university = '''she said,
i took admission in
"bahria univerity"
in cs department'''
print(university)
for character in university:
    print(character)
    for character in apple:
        print(character)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
friend = "neha"
age = 19
career =" medical"
print("my friend name is",friend,"and she is",19, "years old and she dreams to study", career,)
print('hello world')
vegetable = "tomatoe"
print(len(vegetable))
print(vegetable[0:5])
print(vegetable[-4:-1])
 #friend = input()
 #print("My friend name is" ,friend[0:4])
 #age = input("Her age is :" )
print("My friend name is",friend, "and her age is",age,)
print('he said, his name is"zain"')
name = "123456789"
print(len(name))
print(name[0:10])
print(name[-5:-3])
str1 = "  ifrah farooq!!!  "
print(str1.upper())
print(str1.lower())
print(str1.rstrip("!"))
print(str1.strip())
print(str1.replace("i" , "e"))
print(str1.split())
print(str1.center(50))
print(str1.count("f"))
print(str1.endswith("!"))
print(str1.endswith("q"))
print(str1.endswith(" "))
print(str1.find("o"))
print(str1.find("U"))
str2 = "IFRAHFAROOQ05"
print(str2.isalnum())
print(str2.isalpha())
print(str2.islower())
print(str2.isspace())
print(str2.isprintable())
print(str2.istitle())
str3 = "05Ifrah FaRooq"
print(str3.startswith("05Ifrah"))
print(str3.swapcase())
print(str3.title())
print(str1.isupper())
print(str2.isupper())
print(str3.isupper())
 #d = int(input("enter number: "))
 #if(d==18):
   # print("you can drive")
 #elif(d>18):
    #print("you can definitely drive")
 #else:
   # print("you cannot drive")
 #friend = input()
 #if(friend=="neha"):
    #print("My best friend name is", friend,)
 #elif(friend=="nabiha"):
    #print("my best friend sister name is",friend,)
# print("no i dont know her")
#lipstick = 5000
#### print("i am super rich")
#else:
    #print("i am unemployed")
#x =int(input())
#if(x==18):
 #       print("apply for cnic")
#elif(x<=18):
 #       print("you are under 18")
#else:
 #       print("you already have a cnic card")
x = ("call POLICE 15")
print(x.swapcase())
print(x.strip())
print(x.rstrip("15"))
print(x.find("P"))
print(x.isalnum())
print(x.isalpha())
print(x.lower())
print(x.upper())
print(x.center(50))
print(len(x))
for character in x:
    print(character)
    print(x[0:4])
    print(x[5])
#exercise good morning sir
time = ("7:00 pm")
if(time== "12:00 am"):
    print("good afternoon sir")
elif(time=="12:00 pm"):
    print("good night sir")
elif(time=="8:00 am"):
    print("good morning sir")
else:
    print("good evening sir")
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
#match x:
   #case 0: 
    #   print("num is 0")
   ##    print("num is 1")
   #case 4:
    #   print("num is 4")  
for k in range(1,12,3):
    print(k)
for m in range(1,50,10):
    print(m)
for a in range(1,21):
    print(a)   
z = "hassan raheem"
y = True
t = 19
print("the type of z is" , type (z))
print("the type of y is" , type (y))
print("the type of t is" , type (t))
print("my name is Ifrah\nand i study cs")
print("my name is \"ifrah\" and i study cs")
print('my name is "ifrah" and i study cs')
h = 90
j = 10
print(" the sum of a h and j is" ,(90+10))
print(" the subtraction of a h and j is" ,(90-10))
print(" the division of a h and j is" ,(90/10))
print(" the modulus of a h and j is" ,(90%10))
print(" the exponential of a h and j is" ,(90**10))
print(" the floor division of a h and j is" ,(90//10))
p = ("7")
y = ("8")
print( p+y)
print(''' i am ifrah
 and i study cs
 i took a gap year''')
career = "computer science"
print( career[6])
print( career[0:9])
for characters in career:
    print(characters)
print(len(career))
name = "ned university since 1990"
print(name.strip())
print(name.rstrip("since 1990"))
print(name.lower())
print(name.upper())
print(name.islower())
print(name.isupper())
print(name.capitalize())
print(name.title())
print(name.istitle())
print(name.replace("1990", "1998"))
print(name.isalnum())
print(name.isalpha())
print(name.count("e"))
print(name.startswith("N"))
print(name.endswith("0"))
print(name.split())
print(name.center(25))
print("hw")
name = ("obair")
for i in name:
    print(i)
seema=["orange","pink","red"]
for color in seema:
    print(color)
    for i in color:
        print(i)
for m in range(5):
    print(m+2)
for c in range(1,11):
    print(c)
kingdom =("amphibia")
for l in kingdom :
    print(l)
seasons = ("winter","summers","autumn","spring")
for season in seasons:
    print(season, end=",")
    for i in season:
        print(i)
for x in range(5*2,5*3):
    print(x)
for r in range(5+8,5*3):
    print(r+1)
for u in range(11,20,6):
    print(u)
for step in range(2,20,2):
    print(step)
for table in range(17,72,17):
    print(table)
#while loop
for i in range (3):
    print(i)
i = 0
while(i<=3):
    print(i)
    i = i +3
#g = input()
#h=g.isalpha()
#   print(g.upper())
#else:
 #   print("invalid input")
#name= input("enter your name: ")
#j = name.replace(" ","")
#print(len(j))
#a = input()
#b=(a.replace(" ",""))
#print(len(b))
#a = input()
#if a.isalpha():
 #   print(a.upper())
#else:
  #  print("invalid input")
a= input("enter your full name: ")
b =(a.replace(" ",""))
print(len(b))
#ALL LECTURES FROM 1-19 ^
