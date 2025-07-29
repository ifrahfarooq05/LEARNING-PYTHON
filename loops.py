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
