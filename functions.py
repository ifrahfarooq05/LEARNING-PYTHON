#LECTURE 20
#CALCULATING GEOMETRIC MEAN USING DEF FUNCTION:
def calculatingGmean (a,b):
   mean= a*b/(a+b)
   print(mean)

def isGreater (a,b) :
   if a>b:
      print("first number is greater")
   else:
      print("second number is greater or equal ")
#Q1
a = 3
b = 6
calculatingGmean(a,b)
isGreater(a,b)
#Q2
c= 9
d= 2
calculatingGmean(c,d)
isGreater (c,d)
#USING DEF FUNCTION TO IDENTIFY A NUMBER IS EVEN OR ODD
def even_odd(a):
   if a%2==0:
      print("number is even")
   else:
      print("number is odd")

i= 6
even_odd(i)
v=3
even_odd(v)
h=7843648783
even_odd(h)
# Write a function to return the maximum of three numbers
def max_of_three (a,b,c):
   if a>b and a>c:
      print("The greatest number is: ",(a))
   elif b>a and b>c:
      print("the greatest nummber is: ",(b))
   elif c>a and c>b:
      print('The greatest number is: ',(c))

m=24
n=113
o=15
max_of_three(m,n,o)
g=21
h=92
j=71
max_of_three(g,h,j)
#Write a function that returns the length of a given string
def len_string(a):
    print(len(a))
   
name= "ifrah farooq"
len_string(name)
career= "cs"
len_string(career)
hobby= "dancing"
len_string(hobby)
religion= "islam"
len_string(religion)
#CALCULATING MEAN USING DEFINITE FUNCTION.
def average (a=8,b=7,c=1):
   print("the average of given numbers is: ", (a+b+c)/3)

m = 2
n = 9
o = 8
average(m,n,o)   #present  values of the variable will be taken.
#default argument!

a =3
average(a=3) #value of b,c was not given, so default value must be taken.

a=5
b=7
average(a,b)#value of c was taken by default 
#to find average of infinite numbers.
def average(*numbers):
   sum=0
   for i in numbers:
      sum=sum+i
   return  sum/len(numbers)

m=3
f=4
d=7
r=3
t=average(m,f,d,r)  #here t compute and store the average using return  
print(t)
g=9
e=3
w=2
n=average(g,e,w) 
print(n)
#Write a function greet(name) that prints a greeting message
#like "Hello, Alice!".)
def greet(name):
   print("hello,",name,"!")

greet("ifrah")
greet("zain")
greet("obair")
greet("To the person i love most")

#Write a function print_full_name(first_name, last_name) 
# that prints the full name.
def full_name (first_name='ifrah' ,last_name='farooq'):
   print("My good name is",first_name,last_name)

full_name("obair")   #last_name is taken by default
full_name() #by default
full_name('seema','khaleeq')

#LECTURE 30
#RECURSION IN PYTHON:
#IN PYTHON,  a function can call other function and it can call ise;f too.
def factorial(n):
   if (n==0 or n==1):
      return 1
   else:
      return n* factorial(n-1)
   
print(factorial(5))   #5*4*3*2*1 (this is how factorial is!)
print(factorial(0))   #factorial of 0=1
print(factorial(8))   #8*7*6*5*4*3*2*1

#write a program to print fabonacci sequence.
#f0=0        #0,1,1,2,3,5,8,13
#f1=1
#f2=f1+f0
#fn= f(n-1)+f(n-2)
def print_fibonacci_series(n_terms):
    """
    Prints the Fibonacci series up to n_terms.

    Args:
        n_terms (int): The number of terms in the Fibonacci series to print.
    """
    if n_terms <= 0:
        print("Please enter a positive integer for the number of terms.")
        return

    a, b = 0, 1  # Initialize the first two Fibonacci numbers

    if n_terms == 1:
        print(a)
    else:
        print(a, end=" ")  # Print the first term
        print(b, end=" ")  # Print the second term

        for _ in range(2, n_terms):  # Iterate from the third term onwards
            next_term = a + b
            print(next_term, end=" ")
            a = b
            b = next_term

# Example usage:
num_terms = int(input("Enter the number of terms for the Fibonacci series: "))
print_fibonacci_series(num_terms)
print() # Add a newline for better formatting after the series
          