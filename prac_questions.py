#finding all prime numbers till n(user input):
#When checking if a number is prime, you only need to check for divisibility up to its square root, not all the way up to the number itself.
def prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True    

a = int(input("Enter a number: "))
print(f"Prime numbers upto {a}: ")        
for i in range(2,a+1):
    if prime(i):
        print(i, end=',')