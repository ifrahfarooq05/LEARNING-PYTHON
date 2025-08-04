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

