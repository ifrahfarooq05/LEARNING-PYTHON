#LECTURE 36 EXCEPTION HANDLING IN PYTHON:
#a= (input("enter a number: "))
a = "anaconda"
print("The multiplication table of",a,"is: ")
try:
    for i in range (1,6):
        print(f"{int(a)} x {(i)} = {int(a)*i}")

except :
    print("invalid input")
print("done with first question")    
print("finally")
name= 9999
try:
    for i in name:
        print(i)
except Exception as p: 
    print(p)       

l =[13,23,345,52,63]
try:
    print(l[3])
    print(l[7])
except IndexError:
    print("Index no present ")

#LECTURE 37 FINALLY CLAUSE:
def func():
    try:
        l2=[23,44,89,100]
        n = int(input("enter index: "))
        print(l2[n])
        return 0
    except:
        print("Some error occured")
        return 1
    finally:
        print("No matter what finally will always be executed")

#p = func()
#print(p)

#LECTURE 38 RASING CUSTOM ERRORS:
def func2():
    m= int(input("Enter a number between 5 and 9: "))
    if m>9 or m<5:
        raise ValueError("Value should be between 5 and 9")
    print("good")
    
#y=func2()
#print(y)
def func3():
   
     m= (input(" number between 5 and 9: "))
     if  m=="quit":
        print("welldone")
        
     elif (int(m)>5 or int(m)<9):
        raise ValueError("enter num btw 5 and 9 or write quit")    
    
y= func3()
print(y)    
