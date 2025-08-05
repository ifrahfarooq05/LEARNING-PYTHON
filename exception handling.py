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